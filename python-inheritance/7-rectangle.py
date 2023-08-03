#!/usr/bin/python3
"""RECTANGLE CLASS"""
class BaseGeometry:
    """basegeometry class"""
    def area(self):
        """method area to get result"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator to determine whether an integer or not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """rectangle inheritance"""

    def __init__(self, width, height):
        """inheritor instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
    def area(self):
        """calculates and return the area of the rectangle"""
        return self.__width * self.__height

    

    def __str__(self):
        """methoed representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    

r = Rectangle(3, 5)
"""inputing the values"""

print(r)
print(r.area())