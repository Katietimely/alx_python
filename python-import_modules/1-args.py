#!/usr/bin/pyhon3


import sys

if __name__ == "__main__":
     num_args = len(sys.argv) - 1

     if num_args == 0:
          print("0 arguements.")
     
     elif num_args == 1:
          print("1 argument:")

     else:
          print("{} arguements:".format(num_args))
              

     if num_args > 0:
        for num in range(1, len(sys.argv)):
           print("{}:{[num]}".format(num, sys.argv))