from PIL import Image
from load_image import ft_load
import numpy as np


def main():
    try:
        img_array = ft_load("animal.jpeg")
        transpose_img = np.zeros((img_array.shape[1], img_array.shape[0]),
                                 dtype=np.uint8)
        for a in range(img_array.shape[0]):
            for b in range(img_array.shape[1]):
                transpose_img[a][b] = img_array[b][a]
        print(transpose_img)
        img = Image.fromarray(transpose_img, 'L')
        img.show()
    except (FileNotFoundError, IOError, TypeError) as msg:
        print(msg)


if __name__ == "__main__":
    main()
