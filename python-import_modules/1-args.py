#!/usr/bin/python3


from main import argv

def main():
    argv_lens = len(argv) - 1
    print()

    if argv_lens == 0:
        print("0 arguements.")
    elif argv_lens == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(argv_lens))

     
    if argv_lens > 0:
       for i, arg in enumerate(argv[1:], 1):
          print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()


              
     