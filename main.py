import json
import csv
from article import Article
from journal import Jounal
all_articles = []
all_journals = []


def read_JSON(path):
    with open(path, encoding='utf-8') as fh:
        articles_data = json.load(fh)
    return articles_data

def write_dictonary_to_csv(filename, dictonary):
     with open(filename, 'w', encoding="utf-8") as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in dictonary.items():
            writer.writerow([key, value])

def create_dictionary_of_words(all_articles):
    
    word_count = {}

    for article in all_articles:

        title_words = article.get_splited_title()

    for word in title_words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
    

if __name__ == '__main__':
    
    articles_data = read_JSON('data/scholars.json')
    journals_data = read_JSON('data/journals.json')

    for author in articles_data:
        for paper in author["articles"]:
            all_articles.append(Article(paper["title"]))

    for journal in journals_data["articles"]:
        # print(journal["articleTitle"])
        all_journals.append(Jounal(journal["articleTitle"]))


    word_count = create_dictionary_of_words(all_articles + all_journals)

    write_dictonary_to_csv("word_dictionary_v2.csv",word_count)





# with open('words_dictionary.csv', 'w', encoding="utf-8") as csv_file:  
#     writer = csv.writer(csv_file)
#     for key, value in word_count.items():
#        writer.writerow([key, value])

# with open('testF.csv', 'w', encoding="utf-8") as f:
#     for key in word_count.keys():
#         f.write("%s,%s\n"%(key,word_count[key]))

# import matplotlib.pyplot as plt

# plt.bar(range(len(word_count)), list(word_count.values()), align='center')
# plt.xticks(range(len(word_count)), list(word_count.keys()))
# plt.show()