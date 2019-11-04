from sys import argv

ARG_LIMIT = 3

def main():
    argc = len(argv)

    def print_usage():
        print("Example:\n" + "\tpython operations.py 10 3")

    if argc != ARG_LIMIT:
        if argc > ARG_LIMIT:
            print("InputError: too many arguments")

        print_usage()
        exit(1)

    try:
        args = list(map(int, argv[1:]))
    except ValueError:
        print("InputError: only numbers")
        print_usage()
        exit(2)

    print(f"Sum:\t\t {args[0] + args[1]}")
    print(f"Difference:\t {args[0] - args[1]}")
    print(f"Product:\t {args[0] * args[1]}")
    print(f"Quotient:\t {'ERROR (div by zero)' if args[1] == 0 else args[0] / args[1]}")
    print(f"Remainder:\t {'ERROR (modulo by zero)' if args[1] == 0 else args[0] % args[1]}")








if __name__ == "__main__":
    main()