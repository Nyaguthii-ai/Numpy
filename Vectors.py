import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------
# This file contains a function to plot vectors in 2D space using Matplotlib.
def plot_vectors(list_v, list_label, list_color):
    _, ax = plt.subplots(figsize=(10, 10))
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xticks(np.arange(-10, 10))
    ax.set_yticks(np.arange(-10, 10))
    
    
    plt.axis([-10, 10, -10, 10])
    for i, v in enumerate(list_v):
        sgn = 0.4 * np.array([[1] if i==0 else [i] for i in np.sign(v)])
        plt.quiver(v[0], v[1], color=list_color[i], angles='xy', scale_units='xy', scale=1)
        ax.text(v[0]-0.2+sgn[0], v[1]-0.2+sgn[1], list_label[i], fontsize=14, color=list_color[i])

    plt.grid()
    plt.gca().set_aspect("equal")
    plt.show()

v = np.array([[1],[3]])
# Arguments: list of vectors as NumPy arrays, labels, colors.
plot_vectors([v], [f"$v$"], ["black"])

# Example usage: plot the vector v, its double, and its negative double.
plot_vectors([v, 2*v, -2*v], [f"$v$", f"$2v$", f"$-2v$"], ["black", "green", "blue"])

# ---------------------------------------------------------------------------------------
# Example usage: plot the vectors v, w, and their sum v + w.
v = np.array([[1],[3]])
w = np.array([[4],[-1]])

plot_vectors([v, w, v + w], [f"$v$", f"$w$", f"$v + w$"], ["black", "black", "red"])
# plot_vectors([v, w, np.add(v, w)], [f"$v$", f"$w$", f"$v + w$"], ["black", "black", "red"])

# ---------------------------------------------------------------------------------------
# Norm of a Vector
print("Norm of a vector v is", np.linalg.norm(v))

# ---------------------------------------------------------------------------------------
# Dot Product using Python
x = [1, -2, -5]
y = [4, 3, -1]

# define vectors as `NumPy` arrays to avoid errors
x = np.array(x)
y = np.array(y)

# Next, let’s define a function `dot(x,y)` for the dot product calculation:
def dot(x, y):
    s=0
    for xi, yi in zip(x, y):
        s += xi * yi
    return s

print("The dot product of x and y is", dot(x, y))
# or using numpy
print("np.dot(x,y) function returns dot product of x and y:", np.dot(x, y)) 
# or using the explicit operator @ for dot product
print("This line output is a dot product of x and y: ", np.array(x) @ np.array(y))

print("\nThis line output is an error:")
try:
    print(x @ y)
except TypeError as err:
    print(err)

# ---------------------------------------------------------------------------------------
# Speed of Calculations in Vectorized Form
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Use `time.time()` function to evaluate amount of time (in seconds) required to calculate dot 
# product using the function `dot(x,y)` which you defined above: 
tic = time.time()
c = dot(a,b)
toc = time.time()
print("Dot product: ", c)
print ("Time for the loop version:" + str(1000*(toc-tic)) + " ms")
# Output: Time for the loop version:121.83451652526855 ms

# Now compare it with the speed of the vectorized versions
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print("Dot product: ", c)
print ("Time for the vectorized version, np.dot() function: " + str(1000*(toc-tic)) + " ms")
# Output: Time for the vectorized version, np.dot() function: 2.8405189514160156 ms

tic = time.time()
c = a @ b
toc = time.time()
print("Dot product: ", c)
print ("Time for the vectorized version, @ function: " + str(1000*(toc-tic)) + " ms")
# Output: Time for the vectorized version, @ function: 0.49948692321777344 ms

# ---------------------------------------------------------------------------------------
# dot product of orthogonal vectors
i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
print("The dot product of i and j is", dot(i, j))
# the dot product is zero, confirming orthogonal
