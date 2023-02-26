import core.Note as note
import json

def write_file():
    pass

def read_file():
    pass




def create_note(data):
    dic = {}
    new_note = note.Note(data["title"], data["message"])
    dic[new_note.id] = []
    dic[new_note.id] = new_note.__dict__

    with open("data/data.json", 'w') as outfile:
        json.dump(dic, outfile, indent=4)
    

def add_note(data):
    new_note = note.Note(data["title"], data["message"])
    
    with open("data/data.json") as json_file:               #ВЫЕНЕСТИ ФУНКЦИЮ СЧИТЫВАНИЯ В ОТДЕЛЬНУЮ ФУНКЦИЮ 
        data = json.load(json_file)
        data[new_note.id] = []
        data[new_note.id] = new_note.__dict__
        with open("data/data.json", 'w') as outfile:
            json.dump(data, outfile, indent=4)