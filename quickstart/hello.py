# import flask class
# instance of this class will be our WSGI application
# DO NOT call app flask.py, this would conflict with Flask
from flask import Flask

# create an instance of the class
# if imported as a module, use '__module__'
# needed so flask knows where to look for templates, static files, etc
app = Flask(__name__)

# route() decorator to tell flask what url should trigger our function
# bind functions to url


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World!'


# Variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show user profile for that user
    return 'User %s' % username


# can use converter to specify type of the argument
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show post with the given id, id is an integer
    print 'POST is %d' % post_id
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show subpath after /path/
    return 'Subpath %s' % subpath
