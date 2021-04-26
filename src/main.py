from flask import Flask
from flask import render_template
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

@app.route('/add/<name>')
def add_person(name):
    actions.add_person(name)
    return render_template('added.html', name=name)
