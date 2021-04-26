from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import actions

app = Flask(__name__)

@app.route('/')
def starting_page():
    return actions.list_of_commands()

@app.route('/info')
def get_info():
    data = actions.get_leaderboard()
    return render_template('leaderboard.html', len=len(data), data=data)

@app.route('/info/<name>')
def get_info_name(name):
    return render_template('person_info.html', name=name, score=actions.get_score(name))

@app.route('/greet/')
@app.route('/greet/<name>')
def greet(name=None):
    return render_template('greeting.html', name=name)

@app.route('/add/<name>/<score>')
def add_method(name=None, score=None):
    if score == None:
        actions.add_person(name)
    else:
        actions.increase_person(name, score)
    return redirect('/info')

@app.route('/add_person', methods=['POST'])
def add_person():
    name = request.form['newName']
    actions.add_person(name)
    return redirect('/info')

@app.route('/increase/<name>', methods=['POST'])
def increase(name):
    actions.increase_person(name, 1)
    return redirect('/info')

@app.route('/decrease/<name>', methods=['POST'])
def decrease(name):
    actions.increase_person(name, -1)
    return redirect('/info')
