#!/usr/bin/env python3

def convert_to_celsius(fahrenheit):
    convert_to_celsius = (fahrenheit - 32) * 5 / 9
    return convert_to_celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))