import sys


def main(arg):
    """takes a string as an argument and encodes it into Morse Code."""
    morse_code = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
        'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',
        'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',
        '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        ' ': '/'
    }
    try:
        morse_string = ""
        assert len(arg) < 3, "AssertionError: the arguments are bad"
        str_list = arg[1].split()
        for str in str_list:
            assert str.isalnum(), "AssertionError: the arguments are bad"
        for char in arg[1]:
            morse_string += morse_code[char.upper()]
            morse_string += ' '
        morse_string.rstrip()
        print(morse_string)
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv)
