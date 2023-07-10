"""
Exercise No. 08

Implementations of the Note and Notebook class are given. Implement a method named display_notes() in the Notebook class
to display the content of all notes of the notes instance attribute to the console.

Create an instance of the Notebook class named notebook. Then, using the new_note() method add two notes to the notebook
with the following content:

    - 'My first note.'
    - 'My second note.'

In response, call display_notes() method on the notebook instance.

Expected result:

    My first note.
    My second note.
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

    def display_notes(self):
        for note in self.notes:
            print(note.content)


notebook = Notebook()

notebook.new_note(Note('My first note.'))
notebook.new_note(Note('My second note.'))
notebook.display_notes()
