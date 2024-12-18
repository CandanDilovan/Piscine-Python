from PIL import Image

import numpy as np


def ft_load(path: str):
    """Load image from input"""
    try:
        img = np.array(Image.open(path))
        return img
    except (FileNotFoundError, IOError, TypeError) as msg:
        print(msg)
