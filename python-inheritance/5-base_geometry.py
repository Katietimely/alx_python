#!/usr/bin/python3
"""RECTANGLE CLASS"""
class BaseGeometry:
    """basegeometry class"""
    def area(self):
        """method area to get result
                  calculates the area
        Raises:
          Exception: with the message "area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method integer_validator to determine whether an integer or not
         Args:
          name(str): the name of the value
          value: the value has to be validated
         Raises:
          TypeError: if the value is not an integer
          ValueError: if the value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))




