"""
this is a square class that inherits a module class rectangle
"""
from models.rectangle import Rectangle
  


class Square(Rectangle):
    """
    This class inherits the attributes of rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the square object  with size , posdition

        Args:
           size(int): The size of the square.
           x(int): the x-coordinates or default becomes 0
           y(int): the y-coordinates or default becomes 0
           id(int): the Id of the square , if not provided another is assigned
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """returns size of square"""
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string of square instance

        Returns:
          str:returns a formatted string
        """
        return ("[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
