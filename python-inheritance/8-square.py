#!/usr/bin/python3
"""RECTANGLE CLASS"""
class BaseGeometry:
    """basegeometry class"""
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    a class of square inheriting from its parent-attributes
    """
    def __init__(self, size):
        """
        A  method to pass out an attribute of size

        Args:
            size(int): the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less then or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

       # I also added this to fix the error
    def __dir__(cls):
        """
        Metaclass fix
        """
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]

    

    
    

