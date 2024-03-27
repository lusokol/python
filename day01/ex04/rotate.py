from load_image import ft_load
from PIL import Image


def print_short(img):
    """
Print array the right way
    """
    print(f"[[{img[0][0]} {img[0][1]} {img[0][2]} ...\
 {img[0][-3]} {img[0][-2]} {img[0][-1]}]")
    print("  ...")
    print(f"[{img[-1][0]} {img[-1][1]} {img[-1][2]} ...\
 {img[-1][-3]} {img[-1][-2]} {img[-1][-1]}]]")


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


def rotate():
    """
Transpose the image, by inverting X and Y axis.
    """
    image = Image.open("zoomed_animal.jpg")
    width, height = image.size
    rotated_image = Image.new(image.mode, (height, width))
    for x in range(width):
        for y in range(height):
            pixel_value = image.getpixel((x, y))
            rotated_image.putpixel((y, x), pixel_value)

    return rotated_image


def main():
    """
Crop the image at the 'path' into 'w' and 'h' size from 'x' and 'y' position.
Then put it in black and white.
Then transpose it (exchange X and Y coordinate in the image).
    """
    path = "./img/animal.jpeg"
    x, y = 650, 300
    w, h = 400, 400
    zoom = 1

    image = Image.open(path)

    img = zoom_at(image, x, y, zoom, w, h)

    img = img.convert("L")
    img.save("zoomed_animal.jpg")

    img = ft_load("zoomed_animal.jpg")

    print_long_L(img)

    img = rotate()
    img.save("rotated_animal.jpg")
    print_short(ft_load("rotated_animal.jpg", 0))
    # img.show()


if __name__ == '__main__':
    main()
