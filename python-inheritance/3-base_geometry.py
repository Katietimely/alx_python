#1/usr/bin/python3
"""module of base geometry"""



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



