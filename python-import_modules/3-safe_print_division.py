#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        return result


a = 12
b = 2
result = safe_print_division(a, b)



a = 12
b = 0
result = safe_print_division(a, b)

a = 10
b = 2
result = safe_print_division(a, b)

a = 0
b = 0
result = safe_print_division(a, b)

a = 0
b = 2
result = safe_print_division(a, b)

a = 10
b = 0
result = safe_print_division(a, b)





