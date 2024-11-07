from P01.ex03.load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except (FileNotFoundError, IOError, TypeError) as msg:
    print(msg)
