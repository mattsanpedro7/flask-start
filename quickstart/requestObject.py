from flask import request, Flask, render_template

app = Flask(__name__)

print(Flask.secret_key)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the cred were invalid
    return render_template('login.html', error=error)