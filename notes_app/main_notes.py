import click
import time
from tqdm import tqdm
import core.notes_core as core


@click.command()
@click.option("-option", help="Option to work with notes: create, add, delete, look, edit.")
@click.option("-title", help="Note title.")
@click.option("-msg", help="Note content.")
@click.option("-id", help="Unique note ID.")

def start(option, title, msg, id):
    match option:
        case "create":
            if(title != None and msg != None):
                data = {"title":title, "message":msg}
                core.create_note(data)
                displays_work_progress()
        case "add":
            if(title != None and msg != None):
                data = {"title":title, "message":msg}
                if(core.add_note(data)):
                    displays_work_progress()
        case "delete":
            if(id != None):
                if(core.delete_note(id)):
                    displays_work_progress()
                else:
                    click.echo(f"ERROR! There is no note with id {id}")
        case "look":
            displays_work_progress()
            core.show_records()
        case "edit":
            if(id != None and title != None and msg != None):
                data = {"id": id, "title":title, "message":msg}
                if(core.edit_note(data)):
                    displays_work_progress()
                else:
                    click.echo(f"ERROR! There is no note with id {id}")
                
def displays_work_progress():
    for i in tqdm([i for i in range(100)]):
        time.sleep(0.00001)
    click.echo("OK!")


if __name__ == '__main__':
    start()