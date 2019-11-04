import string
from sys import argv

ARG_LIMIT = 3

def main():
    argc = len(argv)

    def usage():
        print("Example:\n" + "\tpython filterwords.py string int")

    if argc != ARG_LIMIT:
        if argc > ARG_LIMIT:
            print("ERROR")
        usage()
        exit(1)

    try:
        n = int(argv[2])
        if argv[1].isnumeric():
            raise ValueError()
        filter_str = argv[1]
    except ValueError:
        print("ERROR")
        usage()
        exit(2)

    print([x for x in filter_str.translate(str.maketrans('', '', string.punctuation)).split() if len(x) > n])




if __name__ == "__main__":
    main()