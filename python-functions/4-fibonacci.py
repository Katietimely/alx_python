#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n == 0:
        fb=[]
        return fb
    elif n == 1:
        fb=[1]
        return fb
    else:
        fb = [0, 1]
    for i in range(2, n):
              fb.append(fb[i-1 + fb[i-2]])
    return fb


if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))
