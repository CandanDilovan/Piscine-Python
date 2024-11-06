from PIL import Image
import numpy as np


def show_images(array: np.array):
    """Take an array and turn it into an image"""
    img = Image.fromarray(array, 'RGB')
    img.show()


def ft_invert(array: np.array) -> np.array:
    """Invert the color of an image"""
    new_new_array = np.copy(array)
    new_array = np.zeros((array.shape[0], array.shape[1], array.shape[2]),
                         dtype=np.uint8)
    new_array.fill(255)
    new_new_array = new_array - new_new_array
    show_images(new_new_array)
    return new_new_array


def ft_red(array) -> np.array:
    """Apply a red filter to the image"""
    new_array = np.copy(array)
    new_array[:, :, 1] *= 0
    new_array[:, :, 2] *= 0
    show_images(new_array)
    return new_array


def ft_green(array) -> np.array:
    """Apply a green filter to the image"""
    new_array = np.copy(array)
    new_array[:, :, 0] -= new_array[:, :, 0]
    new_array[:, :, 2] -= new_array[:, :, 2]
    show_images(new_array)
    return new_array


def ft_blue(array) -> np.array:
    """Apply a blue filter to the image"""
    new_array = np.copy(array)
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    show_images(new_array)
    return new_array


def ft_grey(array) -> np.array:
    """Apply a grey filter to the image"""
    img = Image.fromarray(array).convert('L')
    img.show()
    new_array = np.array(img)
    return new_array
