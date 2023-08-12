#!/usr/bin/python3
"""
A base class representing the geometry

this class is intended to be used as a base for other geometry related classes

Public methods:
-area(self): calculate the area of the geometry
 Raises:
   NotImplementedError: this method is not implemented in the class base

-integer_validator(self, name, value): validates an integer value
Parameters:
            name(str): the name of the value being validated
            value: the value to be validated
Raises:
             typeerror: if the value is not an integer
             valueerror: if the value is less than or equal to 0
"""
class BaseGeometry:
    """basegeometry class"""
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    #i imported than writing the whole code
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    a class of square inheriting from its parent-attributes

    Public-methods:
    -__init__(self, size)
    """
    def __init__(self, size):
        """
        A  method to pass out an attribute of size

        Parameter:
            size(int): the size of the square

        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

       # I also added this to fix the error
    def __dir__(cls):
        """
        Metaclass fix
        """
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__']

    

    
    

