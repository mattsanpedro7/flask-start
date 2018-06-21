# import flask class
# instance of this class will be our WSGI application
from flask import Flask

# create an instance of the class
# if imported as a module, use '__module__'
# needed so flask knows where to look for templates, static files, etc
app = Flask(__name__)

# route() decorator to tell flask what url should trigger our function
@app.route('/')
def hello():
    return 'Hello, World!'
