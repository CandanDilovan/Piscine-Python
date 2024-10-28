import sys


def whatis(arg):
    try:
        argl = len(arg)
        assert arg[1].isnumeric(), "AssertionError: argument is not an integer"
        assert argl < 3, "AssertionError: more than one argument is provided"
        if int(arg[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("Im Odd.")
    except AssertionError as msg:
        print(msg)


whatis(sys.argv)
