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

            if word.lower() in word_count:
                word_count[word.lower()] += 1
            else:
                # print(word.lower())
                word_count[word.lower()] = 1

    return word_count

def get_list_of_csv_column(path):
    
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def optimize_dictionary(dictionary):

    minimum=1
    maximum=max(dictionary.values())
    for key in list(dictionary):
        if dictionary[key] == maximum or dictionary[key] == minimum or dictionary[key]== (minimum+1):
            del dictionary[key]
   
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
    
    choosen_words = ["investigation", "method","based","using","effect", "study", "analysis","numerical","experimental"]
    for word in choosen_words:
        del dictionary[word]

def dictionary_creation():
    
    word_count = create_dictionary_of_words(all_articles + all_journals)
    # print(word_count)
    optimize_dictionary(word_count)
    # print(word_count)
    write_dictonary_to_csv("word_dictionary_v2.csv",word_count)


def get_dictionary_from_csv():
    words = {}
   
    with open('source.csv', mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            words[rows[0]] = rows[1]

    return words

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

    # dictionary_creation()
    # word_count = get_dictionary_from_csv()
    word_count = create_dictionary_of_words(all_articles + all_journals)
    # optimize_dictionary(word_count)

    # print(len(all_articles))
    for article in all_articles:
        article.create_vector(word_count)
    for journal in all_journals:
        journal.create_vector(word_count)

    for key in list(word_count):

        sen = "SEM STUDY OF JUTE FIBRES".lower().split()
        # print(sen)
        
        if key in sen:
            print("trueeeeeeeeeeeeeeeeee")
    print("done")

        

    # for article in all_articles:
    #     article.find_cosine_distance(all_journals)


    # print(len(all_journals))
    # all_articles[0].find_cosine_distance(all_journals)

    # print(all_articles[0].get_journals_cosines().values())