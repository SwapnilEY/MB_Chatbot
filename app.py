import base64
import datetime
import json
import os
import re
import string
import random
import logging
import uuid
import traceback
import threading
import concurrent.futures
import tiktoken as tiktoken
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk


from flask import Flask, redirect, request, render_template, send_from_directory, make_response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

from processes.process import fetch_text_from_url, perform_lem,get_processed_text, generate_greeting_response,generate_response


log = logging.getLogger("MB-logs")


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get')
def chatbot():
    
    message = request.args.get('msg')
    
    data_text = fetch_text_from_url("https://en.wikipedia.org/wiki/Mercedes-Benz")

    continue_dialogue = True
 
    while continue_dialogue:
        human_text = message.lower()
        
        if human_text != 'bye':
            if human_text in ["thanks", "thank you very much"]:
                continue_dialogue = False
                response = "ChatBot: Most Welcome"
                return "ChatBot: Most Welcome"
            else:
                if generate_greeting_response(human_text) is not None:
                    response = "ChatBot: " + generate_greeting_response(human_text)
                    return "ChatBot: " + generate_greeting_response(human_text)
                else:
                    response = generate_response(message,data_text)
                    return "ChatBot: " + response
                    
        else:
            continue_dialogue = False
            response = "ChatBot: Goodbye and take care of yourself."
            return response

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)



# @app.route('/get')
# def chatbot_response():
#     # user_input = request.args.get('msg').lower()

#     if user_input != 'bye':
#         if generate_greeting_response(user_input) is not None:
#             return generate_greeting_response(user_input)
#         else:
#             wiki_text = get_wikipedia_text("https://en.wikipedia.org/wiki/Mercedes-Benz")
#             response = get_response(user_input, wiki_text)
#             return response
#     else:
#         return 'Goodbye and take care of yourself.'

# if __name__ == '__main__':
#     app.run(debug=True)
