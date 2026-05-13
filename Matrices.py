import numpy as np
import matplotlib.pyplot as plt
from utils import plot_lines

# our system of linear equations: −x_1 +3x_2 =7, 3x_1 +2x_2 =1,
A = np.array([
        [-1, 3],
        [3, 2]
    ], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

# print(f"Shape of A: {np.shape(A)}")
# print(f"Shape of A: {np.shape(b)}")

# solve for x
x = np.linalg.solve(A, b)

print(f"Solution: {x}")
# -------------------------------------------------------------------------------
# Evaluate for determinant 
d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")

# Representation of the system as a matrix
A_system = np.hstack((A, b.reshape((2, 1))))

print(A_system)

# how to extract a row of a matrix: extract the second row of a matrix
print(A_system[1])

# Plotting the lines represented by the equations
plot_lines(A_system)

# -------------------------------------------------------------------------------
# system with no solutions : -x_1 + 3x_2 = 7, 3x_1 - 9x_2 = 1
A2 = np.array([
        [-1, 3],
        [3, -9]
    ], dtype=np.dtype(float))

b2 = np.array([7, 1], dtype=np.dtype(float))

print("\nMatrix A2:")
print(A2)
print("\nArray b2:")
print(b2)

# determinant
d2 = np.linalg.det(A2)

print(f"Determinant of matrix A2: {d2:.2f}")
# output: determinant of A2 is zero, thus the system cannot have one unique solution. 
# It will either have infinitely many solutions or none. 

# solve for x
x2 = np.linalg.solve(A2, b2)

print(f"Solution: {x2}")

try:
    x_2 = np.linalg.solve(A_2, b_2)
except np.linalg.LinAlgError as err:
    print(err)

# Construct the matrix corresponding to this linear system:
A2_system = np.hstack((A2, b2.reshape((2, 1))))
print(A2_system)

plot_lines(A2_system)
# -------------------------------------------------------------------------------

# System with infinite solutions: -x_1 + 3x_2 = 7, 3x_1 - 9x_2= -21,
b3 = np.array([7, -21], dtype=np.dtype(float))

A3 = np.hstack((A2, b3.reshape((2, 1))))
print(A3)

#determinant of A3_system is zero, so the system has either no solutions or infinitely many solutions
d3 = np.linalg.det(A3
print(f"Determinant of matrix A3: {d3:.2f}")

# plot lines for the system with infinite solutions
plot_lines(A3)
# -------------------------------------------------------------------------------
# Matrix Multiplication

A = np.array([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
print("Matrix A (3 by 3):\n", A)

B = np.array([[2, 2], [5, 7], [4, 4]])
print("Matrix B (3 by 2):\n", B)

# using matmul to multiply
np.matmul(A, B)
# or
A @ B
# -------------------------------------------------------------------------------
#Matrix Convention and Broadcasting
try:
    np.matmul(B, A)
except ValueError as err:
    print(err) # this will raise an error because the inner dimensions do not match for matrix multiplication.

try:
    B @ A
except ValueError as err:
    print(err) # this will raise an error because the inner dimensions do not match for matrix multiplication.

# checking vector shape
x = np.array([1, -2, -5])
y = np.array([4, 3, -1])

print("Shape of vector x:", x.shape)
print("Number of dimensions of vector x:", x.ndim)
print("Shape of vector x, reshaped to a matrix:", x.reshape((3, 1)).shape)
print("Number of dimensions of vector x, reshaped to a matrix:", x.reshape((3, 1)).ndim)

np.matmul(x,y) # this is the dot product of x and y, which is a scalar value.

# if we want to perform matrix multiplication, we need to reshape the vectors to be 2D matrices.
try:
    np.matmul(x.reshape((3, 1)), y.reshape((3, 1)))
except ValueError as err:
    print(err) 
    # this will raise an error because the inner dimensions do not match for matrix multiplication.

# What about np.dot?
np.dot(A, B)
# This broadcasts the dot product operation to all rows and all columns, to get the resultant product matrix.

# it also allows for subtraction using a scalar value.
A - 2