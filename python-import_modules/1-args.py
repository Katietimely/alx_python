#!/usr/bin/python3


from main import argv

if __name__ == "__main__":
  argv_list = argv[1:]
  num_args = len(argv_list)

  if num_args == 0:
    print("0 arguements.")
  else:
    print(f"{num_args} arguement{'s' if num_args > 1 else ''}:")
    for i,arg in enumerate(argv_list,1):
      print(f"{i}: {arg}")

              
     