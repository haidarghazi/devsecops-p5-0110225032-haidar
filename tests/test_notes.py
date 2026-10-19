"""Unit tests for note validation and business logic."""

import unittest

from app.notes import NoteBook
from app.storage import format_note, format_note_count
from app.validation import validate_title


class NoteBookTests(unittest.TestCase):
    def test_add_note_normalizes_title_and_body(self):
        notebook = NoteBook()
        result = notebook.add_note("  Tugas  ", "  Isi catatan  ")
        self.assertEqual(result, {"title": "Tugas", "body": "Isi catatan"})

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_empty_body_is_rejected(self):
        with self.assertRaises(ValueError):
            NoteBook().add_note("Judul", "  ")

    def test_list_notes_does_not_expose_internal_list(self):
        notebook = NoteBook()
        notebook.add_note("A", "B")
        listed = notebook.list_notes()
        listed.clear()
        self.assertEqual(len(notebook.list_notes()), 1)

    def test_format_helpers(self):
        note = {"title": "Demo", "body": "Teks"}
        self.assertEqual(format_note(note), "[Demo]\\nTeks")
        self.assertEqual(format_note_count([note]), "Jumlah catatan: 1")


if __name__ == "__main__":
    unittest.main()
