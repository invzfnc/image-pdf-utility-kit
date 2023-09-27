# convert_to_pdf.py - Convert list of images to PDF

import os
from PIL import Image
from pathlib import Path

Image.MAX_IMAGE_PIXELS = None

def get_im(src):
    """
    Return a list of Image objects from
    - Path to folder containing images
    - List of images
    """
    try:
        if os.path.isdir(src):  # Folder
            if not os.listdir(src):  # Is empty
                return None
            images = [Path(src, f) for f in os.listdir(src)]
        #else:  # Image(s)
        #    images = src
    except TypeError:
        images = src  # Image(s)

    im_list = []  # Image objects
    
    for image in images:
        im = Image.open(image)
        im_list.append(im.convert("RGB"))

    return im_list

def convert_to_pdf(src, dest):
    """
    Convert image(s) to a single PDF.
    
    src: List of images / Folder
    dest: Output PDF path
    """
    im_list = get_im(src)

    if not dest.endswith(".pdf"):
        dest += ".pdf"

    # Save
    cover = im_list.pop(0)
    cover.save(dest, "PDF", resolution=100.0, 
               save_all=True, append_images=im_list)

    # Clean up
    for im in im_list:
        im.close()
    cover.close()


if __name__ == "__main__":
    # Test case: List of images
    src = ["venv/tests/page-1.png", "venv/tests/page-2.png", "venv/tests/page-3.png"]
    dest = "venv/tests/results/images.pdf"
    convert_to_pdf(src, dest)

    # Test case: Single image
    src = ["venv/tests/page-2.png"]
    dest = "venv/tests/results/image.pdf"
    convert_to_pdf(src, dest)

    # Test case: Folder
    src = "venv/tests/images"
    dest = "venv/tests/results/folder.pdf"
    convert_to_pdf(src, dest)
