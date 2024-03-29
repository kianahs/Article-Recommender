import re
import numpy as np
from numpy import linalg as LA
from heapq import nsmallest, nlargest

class Article:

  authors = []

  def __init__(self, title,keywords):

    self.pure_title = title
    self.title = self.extract_title(title)
    self.keywords = []
    for word in keywords:
      self.keywords += word.split()

    self.keywords_lowercase = ' '.join(map(str, [word.lower() for word in self.keywords]))


  def get_splited_context(self):

    return self.title.split() + self.keywords
  
  def add_author(self, author_name):

    self.authors.append(author_name)

  def get_title(self):

    return self.title
  
  def extract_title(self, title):

    qutation_indexes = [m.start() for m in re.finditer('"', title)]
  
    if qutation_indexes:
      article_title = title[qutation_indexes[0]+1:qutation_indexes[1]]
    else:
      article_title = ""

    self.splitedTitle = re.sub(r'[^\w\s]', '', article_title)
    return self.splitedTitle
    
  def calculate_word_occurance(self, word):
   
    return (self.splitedTitle.lower() + self.keywords_lowercase).count(word)
  
  def create_vector(self, dictionary):
    self.vector_list = []

    for key in list(dictionary):
      self.vector_list.append(self.calculate_word_occurance(key))
    
    self.vector = np.array(self.vector_list)
    
    if not np.any(self.vector):
      return -1
    return 0

   
  def get_vector (self):

    return self.vector


  def find_cosine_distance(self, all_journals):

    self.journals_cosines = {}

    for journal in all_journals:
      journal_vector = journal.get_vector()
      self.journals_cosines[journal] = np.dot(self.vector,journal_vector) / (LA.norm(self.vector) * LA.norm(journal_vector))



  def get_journals_cosines(self):
    return self.journals_cosines

  def get_top_nearest_journals(self, count):
    # print(self.title)
    top_journals = nlargest(count, self.journals_cosines, key = self.journals_cosines.get)
    # print(top_journals.values())
    # print(top_journals[0].get_title())
    values =[]
    for journal in top_journals:
      values.append( self.journals_cosines[journal])

    return top_journals,values