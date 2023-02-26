import click
import time
from tqdm import tqdm

import core.notes_core as core

# `python notes.py add --title "новая заметка" –msg "тело новой заметки"`


@click.command()
@click.option("-option", help="Option to work with notes: create, add, delete, look, edit.")
@click.option("-title", help="Note title.")
@click.option("-msg", help="Note content.")
@click.option("-id", help="Unique note ID.")

def start(option, title, msg, id):
    match option:
        case "create":
            data = {"title":title, "message":msg}
            core.create_note(data)
        case "add":
            data = {"title":title, "message":msg}
            core.add_note(data)
        case "delete":
            click.echo(option)
            click.echo(id)

        case "look":
            click.echo(option)
            click.echo(id)
        
        case "edit":
            click.echo(option)
            click.echo(id)
            click.echo(title)
            click.echo(msg)

        
    for i in tqdm([i for i in range(100)]):
        time.sleep(0.00001)
    click.echo("OK!")


if __name__ == '__main__':
    start()