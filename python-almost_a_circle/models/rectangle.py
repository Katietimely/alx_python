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
           
       Args:
         id(int): the id of a rectangle, if not provided a new one is generated
         width(int): the width of a rectangle
         height(int): the height of a rectangle
         x(int): the x-axis of the rectangle's position, taken initially to be zero
         y(int): the y-axis of the rectangle's position, taken initially to be zero

     
     """
     def __init__(self, width, height, x=0, y=0, id=None):
         """
          An public instance of iherit class rectangle

           Args:
         id(int): the id of a rectangle, if not provided a new one is generated
         width(int): the width of a rectangle
         height(int): the height of a rectangle
         x(int): the x-axis of the rectangle's position, taken initially to be zero
         y(int): the y-axis of the rectangle's position, taken initially to be zero

         Raises:
             typerror: the width, height, x and y must be an integer
             valueerror: the width, height, x and y must be > 0
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
         """
         An instance of width


         Raises:
             typerror: the width must be an integer
             valueerror: the width must be > 0
           
         """
         if not isinstance(value, int):
             raise TypeError("{} must be an integer")
         if value <= 0:
             raise ValueError("{} must be > 0")
         self.__width = value

     @property
     def height(self):
         """int: the height of the rectangle"""
         return self.__height
     
     @height.setter
     def height(self, value):
         """
         Raises:
             typerror: the height must be an integer
             valueerror: the height must be > 0
         """
         if not isinstance(value, int):
             raise TypeError("{} must be an integer".format())
         if value <= 0:
             raise ValueError("{} must be > 0".format())
         self.__height = value

     @property
     def x(self):
         """int: the x-axis of the rectangle position"""
         return self.__x
      
     @x.setter
     def x(self, value):
         """
         Raises:
             typerror: the x must be an integer
             valueerror: the x must be >= 0
         """
         if not isinstance(value, int):
             raise TypeError("x must be an integer")
         if value < 0:
             raise ValueError("x must be >= 0")
         self.__x = value

     @property
     def y(self):
         """int: the y-axis of the rectangle position"""
         return self.__y
     
     @y.setter
     def y(self, value):
        """
        Raises:
             typerror: the y must be an integer
             valueerror: the y must be >= 0
        """
        if not isinstance(value, int):
             raise TypeError("{} must be an integer")
        if value < 0:
             raise ValueError("{} must be >= 0")
        self.__y = value


