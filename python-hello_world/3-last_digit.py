import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

output = " Last digit of" + str(number) + "  is  "

if last_digit > 5:
    output += str(last_digit) + "  and is greater than 5"
elif last_digit == 0:
    output += str(last_digit) + "   and is 0"
else:
    output += "  and is less than 6 and not 0"


print(output)