## Representing Systems of Equations as Matrices

### System of Linear Equations

A **system of linear equations** (or **linear system**) is a collection of one or more linear equations involving the same variables. For example:

$$
\begin{cases} 
-x_1+3x_2=7, \\ 3x_1+2x_2=1, \end{cases}\tag{1}
$$

is a system of two equations with two unknown variables $x_1$ and $x_2$. **To solve** a system of linear equations means to find values for the variables $x_1$ and $x_2$ such that all of its equations are simultaneously satisfied.

A linear system is **singular** if it has no unique solution, and otherwise, it is said to be **non-singular**.

### System of Linear Equations as Matrices
In the lecture, you saw that we represented linear systems of equations as matrices. The system $(1)$ represented as a matrix is as follows:

$$
\begin{bmatrix}
-1 & 3 & 7 \\
3 & 2 & 1
\end{bmatrix}
$$ 

Each row represents an equation in the system. The first column represents the coefficients of $x_1$ in the system, the second column represents the coefficients of $x_2$, and the third column represents the constant values on the right side of the equals signs in the equations.

We could further choose to represent the coefficients of the system $(1)$ as its own matrix $A$ as follows:

$$
\begin{bmatrix}
-1 & 3\\
3 & 2
\end{bmatrix}
$$

and the outputs of the system as a vector $b$ like this:

$$
\begin{bmatrix}
7 \\
1
\end{bmatrix}
$$

The `NumPy` linear algebra package provides a quick and reliable way to solve systems of linear equations using the function `np.linalg.solve(A, b)`. Here, $A$ is a matrix, as you've seen previously, where each row represents one equation in the system, and each column corresponds to the variables $x_1$ and $x_2$. $b$ is a 1-D array of the free (right side) coefficients. More information about the `np.linalg.solve()` function can be found in the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).

To find the solution of the system $(1)$, we will simply use the `np.linalg.solve(A, b)` function. The result will be saved in the 1-D array $x$, where the elements correspond to the values of $x_1$ and $x_2$:

### Evaluating Determinant of a Matrix

The matrix $A$ corresponding to the linear system $(1)$ is a **square matrix** - it has the same number of rows and columns. In the case of a square matrix, it is possible to calculate its determinant - a real number which characterizes some properties of the matrix. A linear system containing two (or more) equations with the same number of unknown variables will have one solution if and only if matrix $A$ has a non-zero determinant.

In this course, it's useful to calculate properties like the determinant by hand to develop an intuition for how it is calculated, but these calculations are also easily done by a computer.

Let's calculate the determinant using the `NumPy` linear algebra package. You can do it with the `np.linalg.det(A)` function. More information about it can be found in [the official documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html).

### Visualizing 2x2 Systems as Plotlines
You can see how easy it is to use contemporary packages to solve linear equations and calculate useful properties of matrices like the determinant.

#### - Representation of the system as a matrix

Before you visualize the system $(1)$, you would want to represent the system in a matrix with the form:

$$
\begin{bmatrix}
-1 & 3 & 7 \\
3 & 2 & 1
\end{bmatrix}
$$

To do this, you can either create a new matrix with these values or horizontally stack the $A$ and $b$ matrices you created earlier. Note that the `np.hstack()` function will require you to reshape array $b$ before it is stacked, as its current shape is $(2,)$. The code below includes the `.reshape((2, 1))` command to allow the horizontal stack to be completed.

#### - Graphical Representation of the Solution

A linear equation in two variables (here, $x_1$ and $x_2$) can be represented geometrically by a line in the plane. This is called the **graph of the linear equation**. In the case of the system of two equations, there will be two lines corresponding to each of the equations, and the solution will be the intersection point of those lines.

In the following code, you will define a function `plot_lines()` to plot the lines and use it later to represent the solution which you found earlier. Do not worry if the code in the following cell is not clear - at this stage, it is not important to understand.

### System of Linear Equations with No Solutions
Given another system of linear equations:

$$
\begin{cases} 
-x_1+3x_2=7, \\ 3x_1-9x_2=1, \end{cases}\tag{2}
$$

The determinant is equal to zero, thus the system cannot have one unique solution. It will either have infinitely many solutions or none. The consistency of it will depend on the free coefficients (right-side coefficients). If you run the code to check that the `np.linalg.solve()` function will give an error due to singularity.

### System of Linear Equations with an Infinite Number of Solutions
By changing the free coefficients of the system $(2)$, you can bring it to consistency:

$$
\begin{cases} 
-x_1+3x_2=7, \\ 3x_1-9x_2=-21, \end{cases}\tag{3}
$$

Thus, from the corresponding linear system

$$
\begin{cases} 
-x_1+3x_2=7, \\ 0=0, \end{cases}\tag{4}
$$

the solutions of the linear system $(3)$ are:

$$
x_1=3x_2-7, \tag{5}
$$

where $x_2$ is any real number.

### Matrix Multiplication

If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, the matrix product $C = AB$ (denoted without multiplication signs or dots) is defined to be the $m \times p$ matrix such that 
$c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\ldots+a_{in}b_{nj}=\sum_{k=1}^{n} a_{ik}b_{kj}, \tag{4}$

where $a_{ik}$ are the elements of matrix $A$, $b_{kj}$ are the elements of matrix $B$, and $i = 1, \ldots, m$, $k=1, \ldots, n$, $j = 1, \ldots, p$. In other words, $c_{ij}$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$.

#### Matrix Multiplication using Python

Like with the dot product, there are a few ways to perform matrix multiplication in Python. As discussed in the previous lab, the calculations are more efficient in the vectorized form. Let's discuss the most commonly used functions in the vectorized form.

You can multiply matrices $A$ and $B$ using `NumPy` package function `np.matmul()`. Which will output matrix as a `np.array`. Python operator `@` will also work here giving the same result. 

#### Matrix Convention and Broadcasting

Mathematically, matrix multiplication is defined only if number of the columns of matrix $A$ is equal to the number of the rows of matrix $B$.

Thus, changing the order of matrices when performing the multiplication $BA$ will not work as the above rule does not hold anymore. 

So when using matrix multiplication you will need to be very careful about the dimensions - the number of the columns in the first matrix should match the number of the rows in the second matrix. This is very important for your future understanding of Neural Networks and how they work. 

However, for multiplying of the vectors, `NumPy` has a shortcut. You can define two vectors $x$ and $y$ of the same size (which one can understand as two $3 \times 1$ matrices). 

Following the matrix convention, multiplication of matrices $3 \times 1$ and $3 \times 1$ is not defined.You will see that there is no error and that the result is actually a dot product $x \cdot y\,$! So, vector $x$ was automatically transposed into the vector $1 \times 3$ and matrix multiplication $x^Ty$ was calculated. While this is very convenient, you need to keep in mind such functionality in Python and pay attention to not use it in a wrong way.

You might have a question in you mind: does `np.dot()` function also work for matrix multiplication?

Yes, it works! What actually happens is what is called **broadcasting** in Python: `NumPy` broadcasts this dot product operation to all rows and all columns, you get the resultant product matrix. Broadcasting also works in other cases, for example, subtracting a scalar unit from a matrix, such as: 
$$
\begin{bmatrix}
-1 & 3\\
3 & 2
\end{bmatrix}
- 2
$$

Mathematically, subtraction of the $3 \times 3$ matrix $A$ and a scalar is not defined, but Python broadcasts the scalar, creating a $3 \times 3$ `np.array` and performing subtraction element by element. A practical example of matrix multiplication can be seen in a linear regression model.