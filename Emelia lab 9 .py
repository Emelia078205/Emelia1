import numpy as np

# Task 1: Filtering Arrays with Boolean Indexing
def filter_array(arr, threshold):
    mask = arr > threshold
    return arr[mask]

# Task 2: Handling NaN and Infinity Values
def check_nan_inf(arr):
    nan_mask = np.isnan(arr)
    inf_mask = np.isinf(arr)
    return (nan_mask, inf_mask)

def clean_array(arr):
    cleaned = arr.copy()
    cleaned[np.isnan(cleaned)] = 0
    cleaned[np.isinf(cleaned)] = 9999
    return cleaned

# Task 3: Multiple Condition Filtering
def complex_filter(arr):
    mask = (arr > 10) & (arr < 50) & (arr % 2 == 0)
    return arr[mask]

# Task 4: Matrix Transposition
def transpose_matrix(arr):
    t1 = arr.T
    t2 = np.transpose(arr)
    return t1, t2

def is_symmetric(arr):
    return np.array_equal(arr, arr.T)

# Task 5: Matrix Multiplication with Transpose
def multiply_transpose(A, B):
    res1 = np.dot(A.T, B)
    res2 = np.dot(A, B.T)
    return res1, res2

# Task 6: Trace of a Matrix
def matrix_trace(arr):
    if arr.shape[0] != arr.shape[1]:
        print("Error: Matrix is not square")
        return None
    return np.trace(arr)

# Task 7: Array Concatenation
def concatenate_arrays(arr1, arr2, axis=0):
    return np.concatenate((arr1, arr2), axis=axis)

def stack_arrays(arr1, arr2):
    v = np.vstack((arr1, arr2))
    h = np.hstack((arr1, arr2))
    return v, h

# Task 8: Array Splitting
def split_array(arr, num_splits):
    if len(arr) % num_splits != 0:
        print("Warning: Array cannot be split evenly, using array_split")
        return np.array_split(arr, num_splits)
    return np.split(arr, num_splits)

# Task 9: Comprehensive Array Analysis
def array_analysis(arr):
    transposed = arr.T
    
    if arr.shape[0] == arr.shape[1]:
        tr = np.trace(arr)
    else:
        tr = None
        
    m = np.mean(arr)
    filtered = arr[arr > m]
    
    return transposed, tr, filtered
