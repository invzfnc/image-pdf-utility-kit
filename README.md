# image-pdf-utility-kit
A collection of utilities for working with images and PDFs.

1. **Convert to PDF**: Converts image(s) into a single PDF file
2. **Convert to Images**: Extracts individual images from a PDF file
3. **Remove/Change Background**: Modifies the background (or foreground) pixels of an image

## Usage
**Convert to PDF**  
The `convert_to_pdf` function allows converting to PDF file from:
- Single image, 
- Multiple images, 
- Path to folder, containing images to be converted.
```python
from convert_to_pdf import convert_to_pdf

convert_to_pdf(["img.png"], "output.pdf")
convert_to_pdf(["im-1.png", "im-2.png", "im-3.png"], "output.pdf")
convert_to_pdf("img_folder", "output.pdf")
```

**Convert to Images**  
```python
convert_to_image("Book.pdf", "Extracted")
```

**Remove/Change Background**  
The `change_pixels` function modifies pixels in an image based on specific conditions.

```python
# Changes color of background
from change_pixels import change_pixels

change_pixels("input.jpg", "foreground.png",
              threshold=(150, 150, 150, 255), 
              replacement_color=(250, 235, 215, 255))
```

![Changing background color](https://raw.githubusercontent.com/eve-1010/image-pdf-utility-kit/main/docs/background.png)

```python
# Changes color of font/foreground
from operator import le
from change_pixels import change_pixels

change_pixels("input.jpg", "foreground.png", 
			  threshold=(80, 80, 80, 255), 
			  replacement_color=(128, 128, 0, 255), 
			  compare_func=le)
```

![Changing foreground color](https://raw.githubusercontent.com/eve-1010/image-pdf-utility-kit/main/docs/foreground.png)

To remove background, pass `(r, g, b, 0)` to `replacement_color` (`0` for alpha channel equals transparency)

## Dependencies
See [requirements.txt](requirements.txt)