#!/usr/bin/python3
"""module of distinguishing same class
   
"""
def inherits_from(obj, a_class):
    """method of is_same_class
      obj: this method has an object of obj
      a_class: this method has an object of a_class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class





