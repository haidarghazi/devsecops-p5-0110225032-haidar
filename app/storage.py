"""Small presentation helpers for displaying notes."""


def format_note(note: dict) -> str:
    """Format a note for terminal output."""
    return f'[{note["title"]}]\\n{note["body"]}'


def format_note_count(notes: list) -> str:
    """Return a human-readable note count."""
    count = len(notes)
    return f"Jumlah catatan: {count}"
