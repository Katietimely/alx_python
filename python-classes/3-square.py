#!/usr/bin/python3
"""
module of a square class with private and public attributes
"""
class Square:
     def __init__(self, size=0):
        self.__size = size
        """ this is a method(function) with just one arguement"""

        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, size):
          if not isinstance(size, int):
            raise TypeError("size must be an integer")
          
          if size < 0:
            raise ValueError("size must be >= 0")
          self.__size = size
          
     def area(self):
         return self.__size ** 2
        
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
   my_square.size = "5 feet"
   print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
   print(e)  