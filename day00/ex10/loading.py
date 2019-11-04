import time
import sys

def ft_progress(iter_input):

    sys.stdout

    sys.stdout.write("[%s]" % (" " * len(iter_input)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(iter_input)+1))

    for item in iter_input:
        sys.stdout.write("=")
        sys.stdout.flush()
        yield item

def main():

    listy = range(100)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.1)

    sys.stdout.write("]\n") # this ends the progress bar


if __name__ == "__main__":
    main()