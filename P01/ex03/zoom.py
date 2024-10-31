from PIL import Image
from load_image import ft_load
import numpy as np


def main():
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        new_list = (400, 400, 1)
        img = Image.fromarray(img_array, 'RGB')
        img = img.crop((0, 0, 400, 400))
        img.show()
        print("New shape after slicing: (400, 400, 1) or (400, 400)")
        img = img.convert('L')
        img_array = np.array(img).reshape(new_list)
        print(img_array)
        img.show()
    except (FileNotFoundError, IOError, TypeError) as msg:
        print(msg)


if __name__ == "__main__":
    main()
