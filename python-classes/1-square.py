#!/usr/bin/python3
"""
module of a square class with private and public attributes
"""
class Square:
     def __init__(self, size=0):
        """ this is a method(function) with just one arguement"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

     def area(self):
         """calculate the area """
         return self.__size ** 2
      
     def perimeter(self):
         """claculate the perimeter of the square"""
         return 4 * self.__size
     
     def get_size(self):
         """merhod square"""
         return self.__size
     
     def set_size(self, new_size):
         """method square
         args:new_size(int)
         """
         if not isinstance(new_size, int):
             raise TypeError("size must be an integer")
         if new_size < 0:
             raise ValueError("size must be >= 0")
         self.__size = new_size
         


    
