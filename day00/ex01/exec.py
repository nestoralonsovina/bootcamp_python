import sys

def main():
    if len(sys.argv) < 2:
        exit(1)

    args = sys.argv[1:]

    for (i, arg) in enumerate(args):
        word = ""
        for c in arg[::-1]:
            if c.isalpha():
                if c.isupper():
                    word += c.lower()
                else:
                    word += c.upper()
            else:
                word += c

        args[i] = ''.join(word)

    args.reverse()
    print(' '.join(args))

if __name__ == "__main__":
    main()