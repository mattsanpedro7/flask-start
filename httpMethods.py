# can use methods argument of route() decorator to handle different HTTP methods
from flask import request, Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST function' # do_the_login()
    else:
        return 'GET function' # show_the_login_form()