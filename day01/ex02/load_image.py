import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
Load an image from the specified path and return it as a NumPy array.

ft_load(path: str) -> np.ndarray
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        exit()
    except Exception as e:
        print(f"Error: Failed to open image '{path}'. {e}")
        exit()

    try:
        print(f"The shape of image is: ({img.size[1]}, {img.size[0]}, \
{img.layers})")
    except AttributeError:
        print("Error: Image does not have a 'layers' attribute.")
        exit()

    return np.array(img)
