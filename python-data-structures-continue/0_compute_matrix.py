#!/usr/bin/python3
def compute_matrix(matrix=[]):
    x =[[element**2 for element in row]for row in matrix]
    return x


if __name__=="__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
