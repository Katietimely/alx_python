#!/usr/bin/python3
"""
module of basegeometry meaasage the area
"""
class BaseGeometry:
    """class defined of baseGeometry
      with no methods in it
    """
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
        """
        calculates the area
        Raises:
          Exception: with the message "area not implemented
        """
        raise Exception("area() is not implemented")

