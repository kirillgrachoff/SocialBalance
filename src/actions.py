from flask import render_template
import sqlite3
import os

class Person:
    def __init__(self, name, score):
        self.name = str(name)
        self.score = int(score)

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(PROJECT_ROOT, '..', 'data')
database_name = "database.db"

def execute_database_command(command):
    with sqlite3.connect(os.path.abspath(database_path + '/' + database_name)) as con:
        cur = con.cursor()
        return cur.execute(command)

if not os.path.exists(database_path + '/' + database_name):
    os.system(f"mkdir -p {database_path}")
    os.system(f"touch {database_path + '/' + database_name}")
    execute_database_command('''
    CREATE TABLE users (
        name TEXT PRIMARY KEY, score INTEGER
    )
    ''')

def list_of_commands():
    return render_template('command_list.html')

def add_person(name):
    execute_database_command(f'''
    INSERT INTO users VALUES ("{name}", 0)
    ''')

def get_score(name):
    ans = execute_database_command(f'''
    SELECT score FROM users WHERE name == "{name}"
    ''')
    if not ans:
        return "no such info"
    return ans[0][0]

def get_leaderboard():
    # returns list of Person
    database = execute_database_command('''
    SELECT * FROM users
    ''')
    data = list(map(lambda it: Person(it[0], it[1]), database))
    return sorted(data, key=lambda person: person.score)[::-1]

def increase_person(cur_name, score):
    cur_score_v = execute_database_command(f'''
    SELECT score FROM users WHERE name == "{cur_name}"
    ''')
    cur_score = list(cur_score_v)[0][0]
    execute_database_command(f'''
    UPDATE users SET score = {score + cur_score} WHERE name == "{cur_name}"
    ''')
