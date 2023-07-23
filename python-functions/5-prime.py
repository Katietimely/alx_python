#!/usr/bin/env python3

def is_prime(number):
    if number <= 1:
        return False
    
    if number == 2 or number == 3:
        return True
    
    if number % 2 == 0:
        return False


    for i in range(3, int(number ** 0.5) + 1,2):
        if number % i == 0:
            return False
        else:
           return True

print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))

        