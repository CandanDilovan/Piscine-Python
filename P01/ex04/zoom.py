from PIL import Image
from load_image import ft_load
import numpy as np


def main():
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        

    except (FileNotFoundError, IOError, TypeError) as msg:
        print(msg)


if __name__ == "__main__":
    main()
