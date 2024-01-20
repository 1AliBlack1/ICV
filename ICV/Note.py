import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, created_at=None, updated_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or self.created_at

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'note_id': self.note_id,
            'title': self.title,
            'body': self.body,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }