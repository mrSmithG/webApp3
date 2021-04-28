from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/Home')
def index():
    return render_template('index.html')

@app.route('/user<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/About'.lower())
def aboutPage():
    return render_template('about.html')




