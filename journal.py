import re
import numpy
class Jounal:

  authors = []

  def __init__(self, title):
    self.pure_title = title
    if title == "SEM STUDY OF JUTE FIBRES":
      print("FinDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
      print(self.extract_title(title))
    self.title = self.extract_title(title)


  def get_splited_title(self):

    return self.title.split()
  
  def add_author(self, author_name):

    self.authors.append(author_name)

  def get_title(self):

    return self.title
  
 
  def extract_title(self, title):

    self.splitedTitle = re.sub(r'[^\w\s]', '', title)

    return self.splitedTitle
    

  
  def calculate_word_occurance(self, word):
    # print(type(self.splitedTitle))
    # print(self.splitedTitle)
 
    
    return self.splitedTitle.lower().count(word)
    # return 0


  def create_vector(self, dictionary):
    self.vector_list = []

    for key in list(dictionary):
      self.vector_list.append(self.calculate_word_occurance(key))
    
    self.vector = numpy.array(self.vector_list)
   
  def get_vector (self):

    return self.vector