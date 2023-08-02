#!/usr/bin/python3
"""
module of a square class with private and public attributes
"""
class Square:
     def __init__(self, size=0):
        self.__size = size
        """ this is a method(function) with just one arguement and the getter and setter are 
        used to manage an attribute
        """

        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, value):
          if not isinstance(value, int):
            raise TypeError("size must be an integer")
          
          if value < 0:
            raise ValueError("size must be >= 0")
          self.__size = value
          
     def area(self):
         """A method defining the area of a given space """
         return self.__size ** 2
        
my_square = Square(89)
"""a basic method decribing the attribute my_square and raising an exception"""
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
"""a basic method decribing the attribute my_square and raising an exception"""
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
   my_square.size = "5 feet"
   print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
   print(e)  