import sys


def main(arg):

    """a function which takes a single string argument and displays the sums\
of its upper-case characters, lower-case\
characters, punctuation characters, digits and spaces"""

    try:
        argl = len(arg)
        assert argl < 3, "AssertionError: more than one argument is provided"
        while argl == 1:
            text_count = input("What is the text to count ?\n")
            if text_count:
                arg.append(text_count)
                argl = len(arg)
        total = len(arg[1])
        total_upper = sum(1 for c in arg[1] if c.isupper())
        total_lower = sum(1 for c in arg[1] if c.islower())
        total_punct = sum(1 for c in arg[1] if isPonctuation(c))
        total_space = sum(1 for c in arg[1] if isSpace(c))
        total_num = sum(1 for c in arg[1] if c.isnumeric())

        print('the text contain', total, "characters:\n",
              f"{total_upper} upper letters\n",
              f"{total_lower} lower letters\n",
              f"{total_punct} punctuation marks\n",
              f"{total_space} spaces\n",
              f"{total_num} digits\n",)
    except (AssertionError, Exception, KeyboardInterrupt) as msg:
        print(msg)


def isSpace(c):
    """Return True if char is space"""
    if c == " ":
        return True
    return False


def isPonctuation(c):
    """Return True if char is punctuation mark"""
    if c in ",.;:?!()[]{}'«»-_/" or c == '"':
        return True
    return False


if __name__ == "__main__":
    main(sys.argv)
