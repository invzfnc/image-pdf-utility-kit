# convert_to_image.py - Convert PDF to image(s)

import fitz
from pathlib import Path

def convert_to_image(src: str, dest: str, ext: str="png", dpi: int=300) -> None:
    """
    Convert PDF to image(s).

    Args:
        src: PDF filepath
        dest: Folder to place extracted images

    Returns:
        This function has no return value

    Example:
        convert_to_image("Book.pdf", "Extracted/Book")
    """

    doc = fitz.open(src)

    for page in doc:
        pix = page.get_pixmap(dpi=dpi)
        pix.save(Path(dest, f"page-{page.number + 1}.{ext}"))

