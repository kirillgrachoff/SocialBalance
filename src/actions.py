from flask import render_template
import random

def list_of_commands():
    return render_template('command_list.html')

def add_person(name):
    # TODO database connection
    pass

def get_score(name):
    # TODO database connection
    return random.randint(-100, 100)

class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def get_leaderboard():
    # returns list of Person
    # TODO database connection
    data = [Person('me', 10), Person('you', -10), Person('Alibaba', 100), Person('Troublemaker', -100)]
    return sorted(data, key=lambda person: person.score)[::-1]
