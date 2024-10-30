from load_image import ft_load

try:
    print(ft_load())
except (FileNotFoundError, IOError, TypeError) as msg:
    print(msg)
