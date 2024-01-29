import tweepy
import re
import pickle

from tweepy import OAuthHandler

consumer_key = '0QeJtI4waRRdjT2fQIqjcLPEy'
consumer_secret = 'hqPhXpNDwz1kF4OJBfr9nbQ4MfmLNJN0XoFW0pGkifoHjoKGiN'
access_token = '1251740926164078592-YbZHukJ3PTCFxQVmVN03TF7t1YIiXl'
access_secret = 'F3o1RzagZt7uWXjvfVWIjca9RwKJoiAQmeCFnV6O8kFA6'

bearer_token = "AAAAAAAAAAAAAAAAAAAAALoCKwEAAAAAlanTHxMI%2FrHVA98pbzpyEwKKAQg%3Dldnxsrv30N7C4FCyI6zDfW1u1ew6ApqmFRp80R5mWU7g9khmb7"

client = tweepy.Client(bearer_token)

response = client.search_recent_tweets("megawati -is:retweet lang:en", max_results=100)

# print(response.meta)

list_tweets = []

tweets = response.data

for tweet in tweets:
    #print(tweet.id)
    list_tweets.append(tweet.text)
    

with open("tfidfmodel.pickle", 'rb') as f:
    vectorizer = pickle.load(f)
    
with open('classifier.pickle', 'rb') as f:
    clf = pickle.load(f)
    
clf.predict(vectorizer.transform(['You are very nice person man, have a good life']))

total_pos = 0
total_neg = 0

for tweet in list_tweets:
    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$"," ",tweet)
    tweet = tweet.lower()
    tweet = re.sub(r"s+[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+[a-z]\$"," ",tweet)
    tweet = re.sub(r"^[a-z]\s+"," ",tweet)
    tweet = re.sub(r"\s+"," ",tweet)
    tweet = re.sub(r"\W"," ",tweet)
    tweet = re.sub(r"\d"," ",tweet)
    #tweet = re.sub(r" ","", tweet)
    sent = clf.predict(vectorizer.transform([tweet]).toarray())
    if sent[0] == 1:
        total_pos += 1
    else:
        total_neg += 1
        
#plotting

import matplotlib.pyplot as plt
import numpy as np
objects = ['Positive', 'Negative']
y_pos = np.arange(len(objects))

plt.bar(y_pos,[total_pos,total_neg],alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel("number")
plt.title("positive negative tweets numbers")

plt.show()
    
