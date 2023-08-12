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
    """
    A base class representing geometry

    this class is intended to be used as a base for other geometry
    """
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
     a base class representing geometry
    """
    def __dir__(self):
        """
        customization of the  attributes visible when calling "dir()
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

        
    def area(self):
        """
        calculate the area of geometry
    
        """
        raise Exception("area() is  not implemented")

    def integer_validator(self, name, value):
        """
        validates an integer value.

        Parameters:
            name(str): the name of the value being validated
            value: the value to be validated
        Raises:
             typeerror: if the value is not an integer
             valueerror: if the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
        """
        a class representing a rectangle inheriting Basegeometry

        Public methods:
        - __init__(self, width, height): initialize a rectangle with width and height
        -  area(self): calculate the area of the 
        - __str_(self): returns a string representation of the rectangle
        """
        def __init__(self, width, height):
            """
            initialize a rectangle with width and height

            Parameters:
             width(int): the width of the rectangle 
             height(int): the height of the rectangle
            """
            self.__width = width
            self.__height = height
            self.integer_validator("width", width)
            self.integer_validator("height", height)

        def area(self):
            """
            calculate area of the rectangle

            Returns:
               int: the area of the rectangle (width * height)
            """
            return self.__width * self.__height

        def str(self):
            """ 
             returns a string representation of the rectangle

             Returns:
                str: a string with rectangle description in the format '[Rectangle] <width>/<height>'.
            """
            return f"[Rectangle] {self.__width}/{self.__height}"
