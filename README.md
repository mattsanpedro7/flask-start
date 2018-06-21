# Starting CLI
FLASK_APP=hello.py flask run
# to share/listen to all public IPs
flask run --host=0.0.0.0

# Enable all development features (including debug mode)
* activates debugger
* activates automatic reloader
* enable debug mode on flask app

export FLASK_ENV=development
flask run

# Flask installation 
* pip install -U Flask

## Converter types:
string	(default) accepts any text without a slash
int	    accepts positive integers
float	accepts positive floating point values
path	like string but also accepts slashes
uuid	accepts UUID strings