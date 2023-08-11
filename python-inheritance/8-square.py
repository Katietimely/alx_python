#!/usr/bin/python3
"""RECTANGLE CLASS"""
class BaseGeometry:
    """basegeometry class"""
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A class inheriting the class BaseGeometry
    """
    def __dir__(self): 
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    pass 

    def area(self):
        """method area to get result
        Args:
          name(str): the name of the value
          value: the value has to be validated
         Raises:
          TypeError: if the value is not an integer
          ValueError: if the value 
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator to determine whether an integer or not
        Args:
          name(str): the name of the value
          value: the value has to be validated
         Raises:
          TypeError: if the value is not an integer
          ValueError: if the value i
        """
        if not isinstance(value, int):
            raise TypeEr
    

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

    

    
    

