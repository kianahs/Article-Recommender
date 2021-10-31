import re

class Article:

  authors = []

  def __init__(self, title):

    self.title = self.extract_title(title)
  
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
      
    return re.sub(r'[^\w\s]', '', article_title)
    