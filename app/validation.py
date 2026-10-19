"""Input validation helpers for notes."""


def validate_title(title: str) -> str:
    """Return a normalized title or raise ValueError for invalid input."""
    normalized = title.strip()
    if not normalized:
        raise ValueError("Judul catatan tidak boleh kosong.")
    if len(normalized) > 80:
        raise ValueError("Judul maksimal 80 karakter.")
    return normalized


def validate_body(body: str) -> str:
    """Validate and return the note body."""
    if not body.strip():
        raise ValueError("Isi catatan tidak boleh kosong.")
    if len(body) > 2000:
        raise ValueError("Isi catatan maksimal 2000 karakter.")
    return body.strip()
