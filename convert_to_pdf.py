# convert_to_pdf.py - Convert list of images to PDF

import os
from PIL import Image
from pathlib import Path
from typing import Iterable

Image.MAX_IMAGE_PIXELS = None

def _get_im(src: Iterable[str] | str) -> list[Image]:
    """
    Helper function of convert_to_pdf

    Args:
        src (Iterable[str] | str): List of images or path to folder

    Returns:
        List of PIL.Image objects
    """

    try:
        if os.path.isdir(src):  # Folder
            if not os.listdir(src):  # Empty
                return None
            images = [Path(src, f) for f in os.listdir(src)]
    except TypeError:
        images = src  # Iterable

    im_list = []  # Image objects
    
    for image in images:
        im = Image.open(image)
        im_list.append(im.convert("RGB"))

    return im_list

def convert_to_pdf(src: Iterable[str] | str, dest: str) -> None:
    """
    Convert image(s) to a single PDF.
    
    Args:
        src (Iterable[str] | str): List of images / Folder
        dest (str): Output PDF path

    Returns:
        This function has no return value

    Raises:
        FileNotFoundError if the source file does not exist or folder is empty

    Example:
        convert_to_pdf(["image.png"], "output.pdf")
        convert_to_pdf(["im-1.png", "im-2.png", "im-3.png"], "output.pdf")
        convert_to_pdf("img_folder", "output.pdf")
    """

    im_list = _get_im(src)

    if not im_list:
        raise FileNotFoundError("No image was provided")

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

