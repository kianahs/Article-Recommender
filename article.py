import re
import numpy as np
from numpy import linalg as LA
from scipy import spatial

class Article:

  authors = []

  def __init__(self, title):

    self.pure_title = title
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
    return self.splitedTitle.lower().count(word)
    # return 1


  def create_vector(self, dictionary):
    self.vector_list = []

    for key in list(dictionary):
      # print(key)
      self.vector_list.append(self.calculate_word_occurance(key))
    
    self.vector = np.array(self.vector_list)
    
    if not np.any(self.vector):
      print(self.vector)
      print("article empty")
      print(self.pure_title)

   
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
      if not np.any(journal_vector):
        print("journal empty", journal.get_title())
      # print("journal vector, \n", journal.get_vector())
      # self.journals_cosines[journal] = spatial.distance.cosine(self.vector, journal.get_vector())
      self.journals_cosines[journal] = np.dot(self.vector,journal_vector) / (LA.norm(self.vector) * LA.norm(journal_vector))



  def get_journals_cosines(self):
    return self.journals_cosines