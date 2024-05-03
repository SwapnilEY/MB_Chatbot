

import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
import requests
import re
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def fetch_text_from_url(url_wiki_link):


    get_link = urllib.request.urlopen(url_wiki_link)
    get_link = get_link.read()
    
    data = bs.BeautifulSoup(get_link,'lxml')
    
    data_paragraphs = data.find_all('p')
    global data_text
    data_text = ''
    
    for para in data_paragraphs:
        data_text += para.text
    data_text = data_text.lower()

    data_text = re.sub(r'\[[0-9]*\]', '', data_text)

    return data_text


def perform_lem(tokens):
    wnlem = nltk.stem.WordNetLemmatizer()

    return [wnlem.lemmatize(token) for token in tokens]


def get_processed_text(document):
    
    punctuation_removal = dict((ord(punctuation),None) for punctuation in string.punctuation)
    return perform_lem(nltk.word_tokenize(document.lower().translate(punctuation_removal)))
    




def generate_greeting_response(greeting):

    greeting_inputs = ("hey", "Hi","Good morning", "Good Evening")
    greeting_responses = ["Hi", "How are you", "Welcome","How can I help you"]

    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)
        




def generate_response(user_input,data_text):
    bot_response = ''
    global data_sentence,data_words
    data_sentence = nltk.sent_tokenize(data_text)
    data_words = nltk.word_tokenize(data_text)

    data_sentence.append(user_input)
    # print(data_sentence)
 
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    all_word_vectors = word_vectorizer.fit_transform(data_sentence)
   
    # Calculate cosine similarity between the user input and all other sentences
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
   
    # Get the index of the most similar sentence (excluding the user input itself)
    similar_sentence_index = similar_vector_values.argsort()[0][-2]
 
    # Flatten and sort the similarity scores
    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    print(matched_vector)
    vector_matched = matched_vector[-2]
 
    if vector_matched == 0:
        bot_response = "I am sorry, I could not understand you"
    else:
        bot_response = data_sentence[similar_sentence_index]
   
    return bot_response


# # Print the introductory message
# intro_message = "Hello, I am from Mercedez Benz ChatBot. You can ask me questions about Mercedes Benz"
# # print(intro_message)
 
# continue_dialogue = True
 
# while continue_dialogue:
#     human_text = input().lower()
 
#     if human_text != 'bye':
#         if human_text in ["thanks", "thank you very much"]:
#             continue_dialogue = False
#             print("Mercedes Benz: Most Welcome")
#         else:
#             if generate_greeting_response(human_text) is not None:
#                 print("Mercedes Benz Bot: " + generate_greeting_response(human_text))
#             else:
#                 response = generate_response(human_text)
#                 print("Mercedes Benz: " + response)
#                 data_sentence.remove(human_text)
#     else:
#         continue_dialogue = False
#         print("Mercedes Benz: Goodbye and take care of yourself.")