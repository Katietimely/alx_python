i = 0
j = 1

while i < 9 :
    while j <= 10 :
        if  ((i < j) or (i == j)):
            print("{:02d}", "{:02d}".format(i, j), end =", ")
        elif (i == 8 and j == 9):
           print("\n")
           break
        else :
            print(" ")
        

    j += 1
i += 1
j= i + 1

print("{:02d}, {:02d}".format(i, j))
      
        

