from load_image import ft_load
from PIL import Image


def print_long(img):
    """
Print array the right way
    """
    print("[[", end='')
    print(img[0, 0])
    print(img[0, 1])
    print(img[0, 2])
    print("     ...")
    print(img[-1, -3])
    print(img[-1, -2])
    print(img[-1, -1], end='')
    print(']]')


def print_long_L(img):
    """
Print array the right way
    """
    print(f"[[[{img[0, 0]}]")
    print(f"  [{img[0, 1]}]")
    print(f"  [{img[0, 2]}]")
    print("  ...")
    print(f"  [{img[-1, -3]}]")
    print(f"  [{img[-1, -2]}]")
    print(f"  [{img[-1, -1]}]]]")


def zoom_at(img, x, y, zoom, w, h):
    """
Not really a zoom, more than a crop.
    """
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2,
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)


def main():
    """
Crop the image at the 'path' into 'w' and 'h' size from 'x' and 'y' position.
Then display it.
    """
    path = "./img/animal.jpeg"
    x, y = 650, 300
    w, h = 400, 400
    zoom = 1

    print_long(ft_load(path))

    image = Image.open(path)

    img = zoom_at(image, x, y, zoom, w, h)
    img = img.convert("L")
    img.save("zoomed_animal.jpg")
    print_long_L(ft_load("zoomed_animal.jpg", 'New shape'))
    img.show()


if __name__ == '__main__':
    main()
