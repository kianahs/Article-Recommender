import re
import numpy as np
from numpy import linalg as LA
from scipy import spatial

class Article:

  authors = []

  def __init__(self, title):

    self.title = self.extract_title(title)


  def get_splited_title(self):

    return self.title.split()
  
  def add_author(self, author_name):

    self.authors.append(author_name)

  def get_title(self):

    return self.title
  
  def extract_title(self, title):

    qutation_indexes = [m.start() for m in re.finditer('"', title)]
    # print("indexes", qutation_indexes)

    if qutation_indexes:
      article_title = title[qutation_indexes[0]+1:qutation_indexes[1]]
    else:
      article_title = ""

    self.splitedTitle = re.sub(r'[^\w\s]', '', article_title)

    return self.splitedTitle
    

  def calculate_word_occurance(self, word):
    return self.splitedTitle.count(word)


  def create_vector(self, dictionary):
    self.vector_list = []

    for key in list(dictionary):
      self.vector_list.append(self.calculate_word_occurance(key))
    
    self.vector = np.array(self.vector_list)

   
  def get_vector (self):

    return self.vector


  def find_cosine_distance(self, all_journals):

    # print("article vector, \n", self.vector)

    self.journals_cosines = {}
    # count = 0

    for journal in all_journals:
      # count = count + 1
      # print(count)
      journal_vector = journal.get_vector()
      # print("journal vector, \n", journal.get_vector())
      # self.journals_cosines[journal] = spatial.distance.cosine(self.vector, journal.get_vector())
      self.journals_cosines[journal] = np.dot(self.vector,journal_vector) / (LA.norm(self.vector) * LA.norm(journal_vector))



  def get_journals_cosines(self):
    return self.journals_cosines