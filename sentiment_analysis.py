from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv

countries = ["india", "brazil", "united states"]
queries = ["query1", "query2", "query3", "query4", "query5", "query6"]
evaluators = {"brazil":["brazil", "india", "argentina", "paraguay", "united kingdom", "united states"],
              "india":["india", "brazil", "pakistan", "nepal", "united kingdom", "united states"],
              "united states":["united states", "india", "brazil", "mexico", "canada", "united kingdom"]
             }


def sentiment_analysis():
    sid = SentimentIntensityAnalyzer()

    for country in countries:
        for query in queries:
            for evaluator in evaluators[country]:
                f = open(country + "/" + query + "/suggestions_" + query + "_" + evaluator + ".csv", 'r')
                g = open(country + "/" + query + "/suggestions_" + query + "_" + evaluator + "_sentiments.csv", 'w')

                for record in f:
                    sentence = record.split(",")[1]
                    ss = sid.polarity_scores(sentence)
                    record = record.split("\n")[0]
                    record += ", " + str(ss) + "\n"
                    g.write(record)



sentiment_analysis()
