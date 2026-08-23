import numpy as np

# Task 1: Basic Numpy Operations

# task1a
def create_array(lst):
    return np.array(lst)

# task1b
def array_stats(arr):
    return np.mean(arr), np.median(arr), np.std(arr)

# task1c
def reshape_array(arr, new_shape):
    return arr.reshape(new_shape)

# task1d
def slice_array(arr, start, end, step=1):
    return arr[start:end:step]


# Task 2: Advanced Numpy Functions

# task2a
def matrix_multiplication(A, B):
    return np.dot(A, B)

# task2b
def transpose_matrix(A):
    return np.transpose(A)

# task2c
def inverse_matrix(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Matrix is not invertible"

# task2d
def solve_linear_equations(A, b):
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return "No unique solution"
