# change_background.py - Change pixels of image when condition is met

from PIL import Image
from operator import ge

PAPER = (180, 180, 180, 255)
TRANSPARENT = (0, 0, 0, 0)

def remove_background(src: str, dest: str, 
                      threshold: tuple[int] = PAPER, 
                      compare_func=ge):
    change_pixels(src, dest, threshold=threshold, 
                  compare_func=compare_func,
                  replacement_color=TRANSPARENT)
    """
    Predefined function to make pixels transparent if they exceed the specified
    threshold.

    The default threshold is set to filter out white paper (180, 180, 180, 255).
    """

def change_pixels(src: str, dest: str, threshold: tuple[int], 
                  replacement_color: tuple[int], compare_func=ge):
    """
    Modify pixels in an image based on specific conditions and save
    the result.

    Args:
        src (str):
            Path to original image

        dest (str):
            Path to save result

        threshold (tuple):
            A 4-valued tuple (R, G, B, A) specifying the threshold
            value for each color channel. By default, pixels exceeding
            (operator.ge) this threshold will be modified. The comparison
            behaviour can be altered with the compare_func parameter

        compare_func (function):
            Function to decide whether certain pixel gets replaced.
            Default is operator.gt (>=)

        replacement_color (tuple):
            A 4-valued tuple (R, G, B, A) representing color to 
            replace the pixels that meet the threshold conditions

    Returns:
        This function has no return value

    Example
        change_pixels("original-image.png",
                      "modified-image.png",
                      (180, 180, 180, 255),
                      (0, 0, 0, 0))
        # Remove background / make transparent

        change_pixels("original-image.png",
                      "modified-image.png",
                      threshold=(130, 130, 130, 255),
                      replacement_color=(0, 100, 0, 255),
                      compare_func=le)
        # Change black font to green
    """

    need_replacement = lambda pixel: all(compare_func(p, t) for p, t in zip(pixel, threshold))

    im = Image.open(src)
    im = im.convert("RGBA")

    for x in range(im.width):
        for y in range(im.height):
            pixel = im.getpixel((x, y))
            if need_replacement(pixel):
                im.putpixel((x, y), replacement_color)

    im.save(dest)
