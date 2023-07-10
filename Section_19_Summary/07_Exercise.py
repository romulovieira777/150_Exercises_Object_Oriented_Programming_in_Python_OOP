"""
Exercise no. 07

The Note class (representation of a note) is given. Implement the Notebook class (representation of a notebook with
notes) with two methods:

    - __init__() for creating an instance attribute of the Notebook class named notes (an empty list where the notes
    will be stored).

    - new_note() for creating a new Note object and adding it to the notes list.

Create an instance of the Notebook class named notebook. Then, using the new_note() method add two notes to the notebook
with the following content:

    - 'My first note.'
    - 'My second note.'

In response, print the content of the notes attribute to the console.

Expected result:

    [Note(content='My first note.'), Note(content='My second note.')]
"""
import datetime


class Note:
    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def __repr__(self):
        return f"Note(content='{self.content}')"


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, note):
        self.notes.append(note)


notebook = Notebook()

notebook.new_note(Note('My first note.'))
notebook.new_note(Note('My second note.'))

print(notebook.notes)
