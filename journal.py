import re

class Jounal:

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

    return re.sub(r'[^\w\s]', '', title)
    