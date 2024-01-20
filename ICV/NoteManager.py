import json

from pip._internal.utils import datetime

from ICV.Note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        return note

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title, body)
            return note
        else:
            return None

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            return True
        else:
            return False

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.created_at.date() == date.date()]
        return filtered_notes

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            notes_data = [note.to_dict() for note in self.notes]
            json.dump(notes_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            notes_data = json.load(file)
            self.notes = [Note(**data) for data in notes_data]

if __name__ == "__main__":
    note_manager = NoteManager()

    while True:
        print("\nOptions:")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. View Notes")
        print("5. Filter Notes by Date")
        print("6. Save Notes to File")
        print("7. Load Notes from File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note_manager.add_note(title, body)
            print("Note added successfully.")

        elif choice == '2':
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            if note_manager.edit_note(note_id, title, body):
                print("Note edited successfully.")
            else:
                print("Note not found.")

        elif choice == '3':
            note_id = int(input("Enter note ID to delete: "))
            if note_manager.delete_note(note_id):
                print("Note deleted successfully.")
            else:
                print("Note not found.")

        elif choice == '4':
            for note in note_manager.notes:
                print(f"{note.note_id}. {note.title} - {note.created_at}")

        elif choice == '5':
            date_str = input("Enter date (YYYY-MM-DD) to filter notes: ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                filtered_notes = note_manager.filter_notes_by_date(date)
                for note in filtered_notes:
                    print(f"{note.note_id}. {note.title} - {note.created_at}")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == '6':
            filename = input("Enter filename to save notes: ")
            note_manager.save_to_file(filename)
            print("Notes saved successfully.")

        elif choice == '7':
            filename = input("Enter filename to load notes from: ")
            note_manager.load_from_file(filename)
            print("Notes loaded successfully.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")