import numpy as np
from PIL import Image


def ft_load(path: str, msg: str = "The shape") -> np.ndarray:
    """
Load an image from the specified path and return it as a NumPy array.

ft_load(path: str) -> np.ndarray
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error: Failed to open image '{path}'. {e}")
        return None

    try:
        if (img.layers > 1):
            print(f"{msg} of image is: ({img.size[1]}, {img.size[0]}, \
{img.layers})")
        else:
            print(f"{msg} after slicing: ({img.size[1]}, {img.size[0]}, \
{img.layers}) or ({img.size[1]}, {img.size[0]})")
    except AttributeError:
        print("Error: Image does not have a 'layers' attribute.")
        return None

    return np.array(img)
