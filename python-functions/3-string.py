#!/usr/bin/env python3
def reverse_string(string):
    return string[::-1]


if __name__ == "__main__":
    print(reverse_string("Hello"))
    print(reverse_string(""))
    print(reverse_string("madam"))
    print(reverse_string("Hello,world!"))