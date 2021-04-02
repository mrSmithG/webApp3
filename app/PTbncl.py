import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home') 
def index():
    return '<h1>Welcome home</h1>'
