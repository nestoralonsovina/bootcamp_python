from sys import argv


def main():
    if len(argv) != 2:
        if (len(argv) > 2):
            print("ERROR")
        exit(1)

    try:
        whois = int(argv[1])
    except ValueError:
        print("ERROR")
        exit(1)

    if whois % 2 == 0:
        print("I'm Even.")
    elif whois == 0:
        print("I'm Zero.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()