#!/usr/bin/python3
"""Rectangle class"""
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
        """method area to get result"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator to determine whether an integer or not
           Args:
          name(str): the name of the value
          value: the value has to be validated
         Raises:
          TypeError: if the value is not an integer
          ValueError: if the value is less than 0
        """
        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be an integer".format(name))
        
class Rectangle(BaseGeometry):
    """rectangle inheritance
    """

    def __init__(self, width, height):
        """inheritor instance
        Args:
          width(int): the width of the rectangle
          height(int): the height of the rectangle
        Raises:
           typeerror: if the weight or height is not an integer
           valuerror: if the weight or height is less or equal to 0
        """
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    
    

    

    

