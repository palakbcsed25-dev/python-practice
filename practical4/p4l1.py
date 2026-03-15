import numpy as np

# a) Generate a 4x4 identity matrix
identity_4x4 = np.eye(4, dtype=int)
print("4x4 Identity matrix:")
print(identity_4x4)
print()

# b) Generate two 3x3 matrices filled with random integers from 1 to 9
np.random.seed(0)  # fixed seed for reproducible output
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))

print("Matrix A (3x3 random integers 1-9):")
print(A)
print()
print("Matrix B (3x3 random integers 1-9):")
print(B)
print()

# matrix addition
sum_matrix = A + B
print("A + B:")
print(sum_matrix)
print()

# matrix multiplication
prod_matrix = A.dot(B)
print("A x B (matrix multiplication):")
print(prod_matrix)
