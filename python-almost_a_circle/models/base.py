"""
module base a resource in building other related files
"""
class Base:
    """
    A class of base serves as the class for other classes to keep track of other instances.

    Attribute:
        __nb_objects(int) : private class attribute
        id(int): public class attribute

    
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
         A public instance of "id"
        
        Args:
          id is given a value, if id is not provided,a new id is formed
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects