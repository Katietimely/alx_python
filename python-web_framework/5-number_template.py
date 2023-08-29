"""
this module is called flask and imported from flask
"""
from flask import Flask
from markupdown import escape

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
    text = escape(text).replace('_', ' ')
    return f"C {text}"

# route created to the previous text using app route
@app.route('/Python/', defaults={'text': ' is cool'})
@app.route('/python/<text>',strict_slashes=False)
def python_with_text(text):
    text = escape(text).replace('_', ' ')
    return f"Python {text}"

# route created to by-pass the previous setting
@ap.route('/number/<n>', strict_slashes=False)
def n_integer(n):
    return f"{n} is a number"

    
if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)
    