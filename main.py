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


def get_dictionary_from_csv():
    words = {}
   
    with open('source.csv', mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            words[rows[0]] = rows[1]

    return words


def suggest_journals_to_articles(word_count, top_k):


    for article in all_articles.copy():
        check = article.create_vector(word_count)
        if check == -1 :
            all_articles.remove(article)
            print("article {} removed".format(article.get_title()))
            
    for journal in all_journals.copy():
        check = journal.create_vector(word_count)
        if check == -1 :
            all_journals.remove(journal)
            print("journal {} removed".format(journal.get_title()))

    fp = open("result.txt","w",encoding="utf8",newline='')
    # count = 1
    for article in all_articles:
        # print("****************** article {} *******************".format(count))
        fp.write("\n\n****************** article {} *******************\n\n".format(article.get_title()))
        article.find_cosine_distance(all_journals)
        k_nearests_journals = article.get_top_nearest_journals(top_k)
        for journal in k_nearests_journals:
            fp.write(journal.get_title()+"\n")
    fp.close()
        # count += 1


if __name__ == '__main__':
    
    articles_data = read_JSON('data/scholars.json')
    journals_data = read_JSON('data/journals.json')

    for author in articles_data:
        for paper in author["articles"]:
            all_articles.append(Article(paper["title"]))

    for journal in journals_data["articles"]:
        all_journals.append(Jounal(journal["articleTitle"]))
    
    
    word_count = create_dictionary_of_words(all_articles + all_journals)
    optimize_dictionary(word_count)
    write_dictonary_to_csv("word_dictionary_vf1.csv",word_count)
    # word_count = get_dictionary_from_csv()

    suggest_journals_to_articles(word_count, 5)

    print("The results were successfully written to the text file (result.txt)")
