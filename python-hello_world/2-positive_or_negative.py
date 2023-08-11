import random
number = random.randint(-10, 10)
# YOUR CODE HERE

if number > 0:
   print(str(number) + " is positive",end="\n")
elif number == 0:
   print(str(number) + " is zero",end="\n")
elif number < 0:
   print(str(number) + " is neagative",end="\n")
   
