"""
Class:      SSW-810
Project:    Homework #12
Professor:  James Rowland
Author:     Nick Cohron
Date:       22 November 2017
Brief:      Putting student database on the web.
"""


# Goto 127.0.0.1:5000 (root) to see rendered web page


from flask import Flask

app = Flask(__name__)

@app.route('/')       # call hello_page function when user requests 'hello' page
def hello_page():
    return "Hello world!"  # return any valid HTML to be rendered by browser

@app.route('/Goodbye')
def see_ya():
    return "See you later!"

app.run(debug=True)  # automatically restart webserver if anything changes


# End of file