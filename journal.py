import re
import numpy 
from numpy import linalg as LA
from heapq import nsmallest, nlargest

class Jounal:

  authors = []

  def __init__(self, title, keywords):
    self.pure_title = title
    self.title = self.extract_title(title)
    self.keywords = keywords


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
    
    return self.splitedTitle.lower().count(word)
    

  def create_vector(self, dictionary):
    self.vector_list = []

    for key in list(dictionary):
      self.vector_list.append(self.calculate_word_occurance(key))
    
    self.vector = numpy.array(self.vector_list)
    
    if not numpy.any(self.vector):
       return -1
    return 0
   
  def get_vector (self):

    return self.vector

  def find_cosine_distance(self, all_articles):

    self.articles_cosines = {}

    for article in all_articles:
      article_vector = article.get_vector()
      self.articles_cosines[article]= numpy.dot(self.vector,article_vector) / (LA.norm(self.vector) * LA.norm(article_vector))



  def get_articles_cosines(self):
    return self.articles_cosines

  def get_top_nearest_articles(self, count):
    # print(self.title)
    top_articles = nlargest(count, self.articles_cosines, key = self.articles_cosines.get)
    values =[]
    for article in top_articles:
      values.append( self.articles_cosines[article])
      
    # print(top_articles[0].get_title())
    return top_articles,values



