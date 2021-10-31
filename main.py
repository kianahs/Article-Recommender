import json
from article import Article
all_articles = []

with open('data/scholars.json', encoding='utf-8') as fh:
    data = json.load(fh)

# print(data)

for author in data:
    for paper in author["articles"]:
        all_articles.append(Article(paper["title"]))


for article in all_articles:

    print(article.get_title())