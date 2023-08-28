"""
this module is called flask and imported from flask
"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

#route created at the localhost
@app.route('/', strict_slashes=False)
def hello_hbnb():
# a defined function of hello_hbnb to return a string
    return "Hello HBNB!"

# route created to dislocate the previous setting
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

#route created to the previous route setting
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    decoded_text = unquote(text).replace('_', ' ')
    return "C {}".format(decoded_texts)

#route created to the previous text using app route
@app.route('/Python/', defaults={'text': ' is cool'})
@app.route('/python/<text>',strict_slashes=False)
def python_with_text(text):
    decoded_text = unquote(text).replace('_', ' ')
    return "Python {}".format(decoded_text)


if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)