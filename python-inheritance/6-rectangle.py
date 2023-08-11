#!/usr/bin/python3
"""Rectangle class"""



class BaseGeometry:
    """basegeometry class"""
class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
BaseGeometry = __import__("5-base_geometry").BaseGeometry
        
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
        self._height = super().integer_validator("width", width)
        self._width =  super().integer_validator("height", height)
         #self.integer_validator for width
         #self.integer_validator for height

    def __dir__(cls):
        return [attribute for attribute in super().__dir__ if attribute != '__init_subclass__']
    
    

    

    

