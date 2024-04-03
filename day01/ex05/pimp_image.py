from PIL import Image
import numpy as np


def ft_invert(array):
    """
Inverts the color of the image received.
If a pixel has a (10, 100, 190) RGB,\
 it keep invert every channel by 255 - channel\
  => (255-10, 255-100, 255-190) => (245, 155, 65)
    """
    img = 255 - array
    Image.fromarray(img).show()
    Image.fromarray(img).save("filtered_img/landscape_inverted.jpg")


def ft_red(array):
    """
Keep only the red color of the image received.
If a pixel has a (10, 100, 190) RGB,\
 it keep only the red channel => (10, 0, 0)
    """
    chan_red = array[:, :, 0]
    img = np.zeros_like(array)
    img[:, :, 0] = chan_red
    Image.fromarray(img).show()
    Image.fromarray(img).save("filtered_img/landscape_red.jpg")


def ft_green(array):
    """
Keep only the green color of the image received.
If a pixel has a (10, 100, 190) RGB,\
 it keep only the green channel => (0, 100, 0)
    """
    chan_green = array[:, :, 1]
    img = np.zeros_like(array)
    img[:, :, 1] = chan_green
    Image.fromarray(img).show()
    Image.fromarray(img).save("filtered_img/landscape_green.jpg")


def ft_blue(array):
    """
Keep only the blue color of the image received.
If a pixel has a (10, 100, 190) RGB,\
 it keep only the blue channel => (0, 0, 190)
    """
    chan_blue = array[:, :, 2]
    img = np.zeros_like(array)
    img[:, :, 2] = chan_blue
    Image.fromarray(img).show()
    Image.fromarray(img).save("filtered_img/landscape_blue.jpg")


def ft_grey(array):
    """
Apply a grey filter which make the average color of every pixel of the\
 image received.
If an pixel has a (10, 100, 190) RGB, average is 100 then the pixel's\
 being => (100, 100, 100)
    """
    grey = np.sum(array, axis=2) / 3
    img = np.zeros_like(array)
    img[:, :, 0] = grey
    img[:, :, 1] = grey
    img[:, :, 2] = grey
    Image.fromarray(img).show()
    Image.fromarray(img).save("filtered_img/landscape_grey.jpg")
