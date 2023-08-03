#!/usr/bin/python3
"""
This class represent a square with a given size

Attribute:
    size(int):The size of the square(private attribute)
"""
class Square:
     """This class represnt a square with a given size
     """
     def __init__(self, size=0):
        """ intialize a square object with an optional size
                  Args:
           size(int): the size of the square(default is 0)
        Raises:
            typeerror:if size is not an integer
            valueerror:if the size is less than  0
          """
        self.__size = size
     def get_size(self):
         """Gets size of the square
            
           Return:
           int: the size of the square
         """
         return self.__size  
