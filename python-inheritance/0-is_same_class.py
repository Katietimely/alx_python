#!/usr/bin/python3
"""module of distinguishing same class
   
"""
def is_same_class(obj, a_class):
    """method of is_same_class
      obj: this method has an object of obj
      a_class: this method has an object of a_class
    """
    return type(obj) is a_class

