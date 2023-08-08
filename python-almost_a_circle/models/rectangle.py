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

class Rectangle(Base):
     """
     A class of rectangle inherits the  class Base and its attributes

     Attributes:
         id(int): the id of a rectangle
         width(int): the width of a rectangle
         height(int): the height of a rectangle
         x(int): the x-axis of the rectangle's position
         y(int): the y-axis of the rectangle's position
     """
     def __init__(self, width, height, x=0, y=0, id=None):
         """
          An public instance of iherit class rectangle

           Attributes:
         id(int): the id of a rectangle
         width(int): the width of a rectangle
         height(int): the height of a rectangle
         x(int): the x-axis of the rectangle's position
         y(int): the y-axis of the rectangle's position
         """
         super().__init__(id)
         self.width = width
         self.height = height
         self.x = x
         self.y = y

     @property
     def width(self):
         """int: the width of the rectangle"""
         return self.__width
     
     @width.setter
     def width(self, value):
         self.__width = value

     @property
     def height(self):
         """int: the height of the rectangle"""
         return self.__height
     
     @height.setter
     def height(self, value):
         self.__height = value

     @property
     def x(self):
         """int: the x-axis of the rectangle position"""
         return self.__x
      
     @x.setter
     def x(self, value):
         self.__x = value

     @property
     def y(self):
         """int: the y-axis of the rectangle position"""
         return self.__y
     
     @y.setter
     def y(self, value):
         self.__y = value


