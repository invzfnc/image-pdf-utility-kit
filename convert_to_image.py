# convert_to_image.py - Convert PDF to image(s)

import fitz
from pathlib import Path

def convert_to_image(src, dest, ext="png", dpi=300):
    """
    Convert PDF to image(s).

    src: PDF filepath
    dest: Folder to place extracted images
    """
    doc = fitz.open(src)

    for page in doc:
        pix = page.get_pixmap(dpi=dpi)
        pix.save(Path(dest, f"page-{page.number + 1}.{ext}"))


if __name__ == "__main__":
    src = r"Getting Started with Visual Studio 2019.pdf"
    dest = "venv/tests/results"
    convert_to_image(src, dest)

    # Do not convert from pdfs produced by convert_to_pdf
