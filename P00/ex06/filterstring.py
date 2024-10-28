import sys
from ft_filter import ft_filter


def main(arg):
    """accepts two arguments: a string(S), and an integer(N).
    print a list of words from S that have a length greater than N."""
    try:
        assert len(arg) < 4, "AssertionError: the arguments are bad"
        assert not arg[1].isnumeric(), "AssertionError: the arguments are bad"
        str_list = arg[1].split()
        for str in str_list:
            assert str.isalnum(), "AssertionError: Special char in string"
        filtered_tab = ft_filter(lambda str_list: True if len(str_list) >
                                 int(arg[2]) else False, str_list)
        print(list(filtered_tab))
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv)
