#!/usr/bin/pyhon3


from main import argv

if __name__ == "__main__":

     num_args = len(argv) - 1

     
     if num_args == 0:
          print("0 arguements.")
     
     elif num_args == 1:
          print("1 argument:")

     else:
          print("{} arguements:".format(num_args))
              

     if num_args > 0:
        for num in range(1, len(argv)):
           print("{}:{[num]}".format(num, argv))