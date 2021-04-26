from flask import render_template
import random

class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score

database = []

def list_of_commands():
    return render_template('command_list.html')

def add_person(name):
    database.append(Person(name, 0))

def get_score(name):
    try:
        for person in database:
            if person.name == name:
                return person.score
        raise Exception("No such value")
    except Exception:
        return "there's no info about this person"

def get_leaderboard():
    # returns list of Person
    data = database
    return sorted(data, key=lambda person: person.score)[::-1]

def increase_person(name, score):
    try:
        for i in range(len(database)):
            if database[i].name == name:
                database[i].score += int(score)
    except Exception:
        pass
