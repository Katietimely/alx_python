#!/usr/bin/python3
"""
this module has the class square and has private attributes and public attributes
"""
class Square:
     """This class represent a square """
     def __init__(self, size):
        self.__size = size
        """ this is a method(function) with just one arguement"""

if __name__ == "__main__":
    my_square = Square(3)
    """a basic function to a method describing the attribute my_square and raising an exception"""
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
