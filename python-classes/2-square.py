#!/usr/bin/python3
"""
module of a square class with private and public attributes
"""
class Square:
     def __init__(self, size=0):
        self.__size = size
        """ this is a method(function) with just one arguement"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
          self.__size = size

     def area(self):
         """A method defining the area of a given space """
         return self.__size ** 2

my_square_1 = Square(3)
"""a basic method decribing the attribute my_square and raising an exception"""
print("Area:{}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
"""a basic method decribing the attribute my_square and raising an exception"""
print("Area:{}".format(my_square_2.area()))


