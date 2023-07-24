#!/usr/bin/pyhon3

from add import add


def main():

    a = 1
    b = 2

    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()