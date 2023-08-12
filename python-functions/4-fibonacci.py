#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fb =[0]
    if n == 1:
        return fb
    
    fb.append(1)
    for i in range(2, n):
              next_fb = fb[i - 1] + fb[i - 2]
              fb.append(next_fb)

    return fb


if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))
