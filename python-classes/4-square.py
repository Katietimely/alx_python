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
         """A method defining the area of a given space """
         return self.__size * self.__size
     
     def my_print(self):
         """A method defining the size of a given space"""
         if self.__size == 0:
             print()
         else:
             for _ in range(self.__size):
                 print("#" * self.__size)



my_square = Square(3)
"""a basic method to a method describing the attribute my_square and raising an exception"""
my_square.my_print()

print("--")

my_square.size = 10
"""a basic method to a method describing the attribute my_square and raising an exception"""
my_square.my_print()

print("--")

my_square.size = 0
"""a basic method to a method describing the attribute my_square and raising an exception"""
my_square.my_print()

print("--")


        