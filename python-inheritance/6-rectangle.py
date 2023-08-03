#!/usr/bin/python3
"""Rectangle class"""
class BaseGeometry:
    """basegeometry class"""
    def area(self):
        """method area to get result"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator to determine whether an integer or not"""
        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be an integer".format(name))
        
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
"""different values to get the method area"""

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    

