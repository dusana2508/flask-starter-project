from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user/<ime>')
def pozdrav(ime):
    return 'Pozdrav %s' % ime


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return 'Pozdrav {0} je {1}'.format(request.form['zrka'], request.form['tip'])


app.run()
