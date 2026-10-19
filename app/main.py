"""Entry point for the Secure Notes CLI demo."""

from app.notes import NoteBook
from app.storage import format_note, format_note_count


def main() -> None:
    """Run a short interactive session in the terminal."""
    notebook = NoteBook()
    print("=== Secure Notes CLI ===")
    print("Masukkan satu catatan untuk demonstrasi.")
    title = input("Judul: ")
    body = input("Isi: ")
    try:
        notebook.add_note(title, body)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return
    notes = notebook.list_notes()
    print(format_note_count(notes))
    for note in notes:
        print(format_note(note))


if __name__ == "__main__":
    main()
