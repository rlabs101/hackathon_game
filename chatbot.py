#coding: utf-8

import nltk
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import random
import string

f = open('chatbot.txt', 'r', errors = 'ignore')
raw = f.read()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

sent_tokens[:2]


word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalizer(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ["hi", "hello", "greetings", "sup", "what's up", "hey", "whats up"]
GREETING_OUTPUTS = ["hello", "hi", "hey", "*nods*", "I am glad that you are talking to me", "hi there"]


def greeting(sentence):
    for word in sentence.split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_OUTPUTS)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    bot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer = LemNormalizer, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        bot_response += "I am sorry but I do not understand what you are saying"
        return bot_response

    else:
        bot_response += sent_tokens[idx]
        return bot_response

boolBreaker = True

print ("Hi! My name is HealthDesk, and I can talk to you about healthcare services in India.")

while boolBreaker:
    user_response = input("You: ")
    user_response = user_response.lower()

    if user_response == 'bye':
        boolBreaker = False
        print ("Bye! Talk to you soon!")

    else:
        if user_response == 'thanks' or user_response == 'thank you':
            print ("You are welcome")

        elif greeting(user_response) != None:
            print (greeting(user_response))

        else:
            print (response(user_response))
            sent_tokens.remove(user_response)
