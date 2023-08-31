"""
this module is called flask and imported from flask
"""
from flask import Flask
from markupsafe import escape

# using flask module
app = Flask(__name__)

# route created at the localhost
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

#route created to the previous text using app route
@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@ap.route('/python/<text>')
def python_with_text(text):
    text = escape(text).replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)