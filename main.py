from operator import methodcaller
from flask import Flask, render_template, request, jsonify
import os 
import random 

arnold_quotes = ["Let off some steam, Bennett!", "So you cooked up a story and dropped the six of us in a meatgrinder?", "Get to the Choppa!", "Hasta la vista, baby!", "Killian, here's your Subzero, now plain zero!", "What about the guy you lobotimized? Did he get a refund?", "Get your *** to Mars!", "See you at the party Richter!"]

#This gets a random arnold quote
def get_da_quote(quotes_list): 
    random_quote = random.choice(quotes_list)
    return random_quote

app = Flask(__name__)

@app.route('/')
def home():
    return get_da_quote(arnold_quotes)

@app.route('/add', methods = ['POST'])
def add_quote(): 
    print(request.get_json())
    a_quote = request.get_json()['quote']
    arnold_quotes.append(a_quote)
    return jsonify(arnold_quotes)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host = '0.0.0.0', port=port) 