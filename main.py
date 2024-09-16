
# James Folk
# CHEM539
# Assignment 2
# Fall 2024

import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 1000) for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = generate_matrix(20, 20)
B = generate_matrix(20, 20)

C = matrix_multiply(A, B)

print(C)
