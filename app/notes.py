"""Business logic for creating and listing notes."""

from app.validation import validate_body, validate_title


class NoteBook:
    """Keep notes in memory for this simple demonstration application."""

    def __init__(self):
        self._notes = []

    def add_note(self, title: str, body: str) -> dict:
        """Validate and add a note, returning the stored note."""
        note = {
            "title": validate_title(title),
            "body": validate_body(body),
        }
        self._notes.append(note)
        return note.copy()

    def list_notes(self) -> list:
        """Return a copy so callers cannot mutate internal state."""
        return [note.copy() for note in self._notes]
