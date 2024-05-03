## Introduction 📚
The code sets up a Flask web application for a chatbot. It imports various libraries for web development and natural language processing tasks. It initializes Flask, downloads necessary NLTK resources, and defines functions for fetching data from Wikipedia, lemmatizing text, and computing responses based on user input. The application includes routes for the root URL and a route to handle chatbot responses. Depending on the user input, it generates responses. The chatbot's behavior relies on functions like generate_greeting_response() and get_response().


## Function Documentation:

1.	Importing Libraries:
    o	The code begins by importing several Python libraries:
        -   Flask: A web framework for building web applications.
        -   nltk (Natural Language Toolkit): A library for natural language processing tasks.
        -	TfidfVectorizer and cosine_similarity from sklearn: These are used for text vectorization   and similarity calculations.
        -	bs4 (Beautiful Soup): A library for web scraping and parsing HTML content.
        -	Other standard libraries like urllib, re, and string.

2.	Setting Up a Flask Web Application:
    o	The app object is created using Flask(__name__). This initializes a Flask web application.
    o	The code doesn’t show any routes or endpoints, but typically, you would define routes to handle different URLs and HTTP methods (e.g., GET, POST).

3.	Downloading NLTK Resources:
    o	The code downloads NLTK resources (specifically, tokenizers and lemmatizers) using nltk.download('punkt') and nltk.download('wordnet').

4.	Loading Data from Wikipedia:
    o	The get_wikipedia_text(url) function retrieves text data from a Wikipedia page specified by the url.
    o	It fetches the content, extracts paragraphs, converts the text to lowercase, and removes any numeric references (e.g., [1]).

5.	WordNet Lemmatization:
    o	The WordNetLemmatizer is initialized as wnlem.
    o	The process_text(document) function tokenizes the input text, lemmatizes each token, and removes punctuation.
    o	Lemmatization reduces words to their base form (e.g., “running” becomes “run”).

6.	TF-IDF Vectorization:
    o	The get_response(user_input, data) function computes a response based on user input and the Wikipedia data.
    o	It tokenizes sentences, appends the user input, and then uses TfidfVectorizer to transform the tokens into numerical vectors.
    o	Cosine similarity is calculated between the user input vector and all other sentence vectors.
    o	The most similar sentence (excluding the user input) is chosen as the response.

7.	Generating Greeting Responses:
    o	The generate_greeting_response(greeting) function generates a response based on common greetings.
    o	If the input contains a recognized greeting (e.g., “hey,” “good morning”), it selects a random response (e.g., “hi,” “how are you”).

8.	Flask Routes:
    o	The code defines two routes using the @app.route() decorator:
        -	@app.route('/'): This route corresponds to the root URL (“/”). When a user accesses the root URL, the home() function is called.
        -	@app.route('/get'): This route corresponds to the “/get” URL. When a user accesses this URL (e.g., by making an HTTP request), the chatbot_response() function is called.

9.	home() Function:
    o	The home() function is associated with the root URL (“/”). When a user visits the root URL, this function is executed.
    o	Inside the function, render_template('index.html') is called. This typically renders an HTML template (named “index.html”) and sends it as a response to the user’s browser.

10.	chatbot_response() Function:
    o	This function handles requests to the “/get” URL.
    o	It retrieves the user input from the query parameter named “msg” (using request.args.get('msg')).
    o	If the user input is not “bye,” it proceeds with the following logic:
        -	It checks if the user input matches any recognized greeting using the generate_greeting_response(user_input) function.
            1.	If a greeting is recognized, it returns a corresponding response (e.g., “hi,” “how are you”).
            2.	Otherwise, it fetches Wikipedia text related to Mercedes-Benz (from the specified URL) and computes a response using the get_response(user_input, wiki_text) function.
        -	If the user input is “bye,” it returns a farewell message.
    o	The debug=True argument in app.run() enables debugging mode when the script is executed directly (i.e., not imported as a module).
    
11.	Execution:
    o	The final block (if __name__ == '__main__':) ensures that the Flask app runs only if the script is executed directly (not when imported as a module).

Overall, this sets up a basic Flask web application with two routes: one for the root URL and another for handling chatbot responses. Depending on the user input, it either generates a greeting response, fetches information from Wikipedia, or says goodbye. The actual behavior of the chatbot would depend on the implementation of the generate_greeting_response() and get_response() functions.


## Prerequisites 🛠️
Before we get started, make sure you have the following installed on your machine:
- python 3.10 - https://www.python.org/downloads/ - stable versions
- pycharm https://www.jetbrains.com/pycharm/download/other.html - community version 


## Getting Started
- Installation process
   1. GIT: 
      - please select the branch which you want to clone
      - execute this command in CMD from the folder where you want the git repo to be: 
        git clone --branch <branch_name> https://github.com/SwapnilEY/MB_Chatbot.git

  2. Python
     - Go to the folder where git repo is cloned (ref. Step 1).
     - Open CMD in this path.
     - Creating Virtual Environment: python -m venv .venv
     - Activate Environment: .venv\Scripts\activate
     - Install requirements in the environment: pip install -r resources\requirements.txt
     - To the run the application, in terminal type - python app.py

  3. You are ready to go!!



## FYI
- The installation of python requirements might get version conflicts, in such cases please remove the versions from the resources\requirements.txt for the mentioned library and try again.


## Testing model with different questions.
-If you want to test the model with different questions, you can rename "indexs.html" to "index.html" and while doing so rename existing index.html file to something else.
