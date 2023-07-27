#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in row]for row in matrix]
    return new_matrix

matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]

if __name__ == "__main__":
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)