# -*- coding: utf-8 -*-
"""
Created on Sun May 28 20:12:12 2023

@author: HP
"""

import tweepy
import re
import pickle

from tweepy import OAuthHandler

#initialize keys
consumer_key = '0QeJtI4waRRdjT2fQIqjcLPEy'
consumer_secret = 'hqPhXpNDwz1kF4OJBfr9nbQ4MfmLNJN0XoFW0pGkifoHjoKGiN'
access_token = '1251740926164078592-YbZHukJ3PTCFxQVmVN03TF7t1YIiXl'
access_secret = 'F3o1RzagZt7uWXjvfVWIjca9RwKJoiAQmeCFnV6O8kFA6'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#find tweet bout facebook
args = ['alex bhizer']

#will stop if in 10 sec found nothing
api = tweepy.API(auth, timeout=10)

#making list
list_tweets = []

with open('tfidmodel.pickle', 'rb') as f:
    vectorizer = pickle.load(f)
    
with open('classifier.pickle', 'rb') as f:
    clf = pickle.load(f)

query = args[0]
if len(args) == 1:
    for status in tweepy.Cursor(api.search_tweets, q=query+" -filter:retweets", lang='en', result_type= 'recent').items(20):
        list_tweets.append(status.text)