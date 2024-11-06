from PIL import Image

import numpy as np


def ft_load(path: str):
    try:
        pixel = []
        img = Image.open(path)
        img_rgb = img.convert('RGB')
        img_list = (img_rgb.width, img_rgb.height, 3)
        print("The shape of the image is:", img_list)
        for y in range(img_rgb.height):
            for x in range(img_rgb.width):
                r, g, b = img_rgb.getpixel((x, y))
                new_node = [r, g, b]
                pixel.append(new_node)
        real_array = np.array(pixel).reshape(img_list)
        return real_array
    except (FileNotFoundError, IOError, TypeError) as msg:
        print(msg)

