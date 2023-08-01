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
         return self.__size * self.__size
     
     def my_print(self):
         if self.__size == 0:
             print()
         else:
             for _ in range(self.__size):
                 print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")


        