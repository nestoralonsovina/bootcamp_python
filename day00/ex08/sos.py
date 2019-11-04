import string
from sys import argv


CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

ARG_LIMIT = 2

def main():
    argc = len(argv)

    if argc < ARG_LIMIT:
        exit(1)

    args = list(map(lambda x: x.upper(), ' '.join(argv[1:]).split()))
    try:
        if not all(map(lambda x: x.isalnum(), args)):
            raise ValueError()
    except ValueError:
        print("ERROR")
        exit(2)

    for (i, word) in enumerate(args):
        morse_word = []
        for c in word:
            morse_word.append(CODE[c])
        args[i] = ' '.join(morse_word)

    print(' / '.join(args))

if __name__ == "__main__":
    main()
