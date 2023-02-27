import core.Note as note
import json
from datetime import datetime

def write_file(dic):
    with open("data/data.json", 'w') as outfile:
        json.dump(dic, outfile, indent=4)


def read_file():
    try:
        with open("data/data.json") as json_file:            
            data = json.load(json_file)
        return data
    except:
        print("ERROR! First create a list of notes with: ... -option create ...")


def create_note(data):
    dic = {}
    new_note = note.Note(data["title"], data["message"])
    dic[new_note.id] = new_note.__dict__
    write_file(dic)


def add_note(data):
    new_note = note.Note(data["title"], data["message"])
    data = read_file()
    if(data != None):
        data[new_note.id] = new_note.__dict__
        write_file(data)
        return True
    

def delete_note(note_id):
    notes = read_file()
    if(notes != None):
        if note_id in notes.keys():
            notes.pop(note_id)
            write_file(notes)
            return True
        else:
            return False    


def show_records():
    notes = read_file()
    if(notes != None):
        sorted_data = sort_by_time(notes)
        for note in sorted_data:
            print(note)


def sort_by_time(data):
    dictionary_with_new_keys = {}
    intermediate_keys = []
    sorted_data = []

    for key in data.keys():
        note = data.get(key)
        time_of_creation = note["_Note__time_create"].split(".")
        new_key = int(time_of_creation[0]) + int(time_of_creation[1]) + int(time_of_creation[2])

        dictionary_with_new_keys[new_key] = note
        intermediate_keys.append(new_key)

    sorted_keys = sorted(intermediate_keys)
    sorted_keys.reverse()

    for key in sorted_keys:
        sorted_data.append(dictionary_with_new_keys.get(key))

    return sorted_data


def edit_note(data):
    notes = read_file()
    if(notes != None):
        if data["id"] in notes.keys():
            time_create = datetime.now()
            time_create = f"{time_create.day}.{time_create.month}.{time_create.year}"

            notes[data["id"]]["_Note__title"] = data["title"]
            notes[data["id"]]["_Note__body"] = data["message"]
            notes[data["id"]]["_Note__time_create"] = time_create

            write_file(notes)

            return True
        else:
            return False    
    