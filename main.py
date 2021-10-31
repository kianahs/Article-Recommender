import json
import csv
from article import Article
all_articles = []
all_journals = []
word_count = {}


with open('data/scholars.json', encoding='utf-8') as fh:
    articles_data = json.load(fh)

# print(articles_data)
with open('data/eejjournal.json', encoding='utf-8') as f:
    journals_data = json.load(f)

for author in articles_data:
    for paper in author["articles"]:
        all_articles.append(Article(paper["title"]))

# for article in journals_data:

for article in all_articles:

    title_words = article.get_splited_title()

    for word in title_words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# print(word_count)
with open('dict.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in word_count.items():
       writer.writerow([key, value])