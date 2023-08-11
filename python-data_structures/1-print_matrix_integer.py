#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, item in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item), end="")
                
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



if __name__ == "__main__":
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

