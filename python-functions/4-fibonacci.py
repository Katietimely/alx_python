#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

        
    return sequence


if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))
