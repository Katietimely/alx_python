#!/usr/bin/python
"""
A base class representing the geometry

this class is imported as a base 
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
    a base class repersenting geometry
    """
    def __dir__(self):
        """
        customization of the  attributes visible when calling "dir()
        """
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
        a class inheriting from basegeometry

        public methods:
          __init__(self, width, height): initialize a rectangle with width and height
          area(self): calculate the area o
          __str_(self): returns a string
        """
        def __init__(self, width, height):
            """
            initialize a rectangle with width and height

            Parameters:
             width(int): the width 
             height(int): the height
            """
            self.__width = width
            self.__height = height
            self.integer_validator("width", width)
            self.integer_validator("height", height)

        def area(self):
            """
            calculate area of a rectangle

            Returns:
               int: the area of the rectangle (width * height)
            """
            return self.__width * self.__height

        def str(self):
            """ 
             returns a string

             Returns:
                str: a string with rectangle description in the format ""[Rectangle] {self.__width}/{self.__height}"
            """
            return f"[Rectangle] {self.__width}/{self.__height}"
