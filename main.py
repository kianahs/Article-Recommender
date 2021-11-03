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
    # with open(filename, 'w', encoding="utf-8") as f:
    #     for key in dictonary.keys():
    #         f.write("%s,%s\n"%(key,word_count[key]))

def create_dictionary_of_words(all_articles):
    
    word_count = {}

    for article in all_articles:

        title_words = article.get_splited_title()

        for word in title_words:

            if word.lower() in word_count:
                word_count[word.lower()] += 1
            else:
                print(word.lower())
                word_count[word.lower()] = 1

    return word_count

def get_list_of_csv_column(path):
    
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def optimize_dictionary(dictionary):

    # import operator
    # key_max = max(dictionary, key= lambda x: dictionary[x])
    # keyMax = max(dictionary.items(), key = operator.itemgetter(1))[0]
    # print(max(dictionary.values()))
    # print(dictionary)
    key_max = max(dictionary, key=dictionary.get)
    key_min = min(dictionary, key=dictionary.get)
    # print(key_max, dictionary[key_max])
    del dictionary[key_max]
    del dictionary[key_min]
    all_prepositions = []
    english_prepositions=get_list_of_csv_column("prepositions.csv")
    # print(prepositions)
    persion_prepositions = ["بوسیله","دادن","شده","بود","است","چند","آن","آنها","ها","برای","تا","جز","از","به","بدون","بر","در","بی","با","چون","مانند","مثل","غیر","روی","بالای","های","شد","شدن","بودن","یا","کردن","ای","هم","هر","اس","ایها","ایهای","دیگر","همراه","که","جزء"]
    for item in english_prepositions:
        all_prepositions.append(item[0])

    all_prepositions += persion_prepositions
    for key in list(dictionary):
   
        if key.isdigit()==True :
            del dictionary[key]
        elif key.lower() in all_prepositions:
             del dictionary[key]
        elif key.isalpha() and len(key) == 1:
            del dictionary[key]
 
            
if __name__ == '__main__':
    # print("A".isdigit())
    
    articles_data = read_JSON('data/scholars.json')
    journals_data = read_JSON('data/journals.json')

    for author in articles_data:
        for paper in author["articles"]:
            all_articles.append(Article(paper["title"]))

    for journal in journals_data["articles"]:
        # print(journal["articleTitle"])
        all_journals.append(Jounal(journal["articleTitle"]))


    word_count = create_dictionary_of_words(all_articles + all_journals)
    # print(word_count)
    optimize_dictionary(word_count)
    # print(word_count)
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