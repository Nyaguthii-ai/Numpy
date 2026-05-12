## Vectors

The vector is defined by its **norm (length, magnitude)** and **direction**, not its actual position. But for clarity and convenience vectors are often plotted starting in the origin (in $\mathbb{R}^2$ it is a point $(0,0)$) 

### Scalar Multiplication and Sum of Vectors
Vectors can be visualized as arrows, and it is easy to do it for a $v\in\mathbb{R}^2$, e.g.
$v=\begin{bmatrix}
          1 & 3
\end{bmatrix}^T$

#### Scalar Multiplication
**Scalar multiplication** of a vector $v=\begin{bmatrix}
          v_1 & v_2 & \ldots & v_n 
\end{bmatrix}^T\in\mathbb{R}^n$ by a scalar $k$ is a vector $kv=\begin{bmatrix}
          kv_1 & kv_2 & \ldots & kv_n 
\end{bmatrix}^T$ (element by element multiplication). If $k>0$, then $kv$ is a vector pointing in the same direction as $v$ and it is $k$ times as long as $v$. If $k=0$, then $kv$ is a zero vector. If $k<0$, vector $kv$ will be pointing in the opposite direction. In Python you can perform this operation with a `*` operator.

#### Sum of Vectors

**Sum of vectors (vector addition)** can be performed by adding the corresponding components of the vectors: if $v=\begin{bmatrix}
          v_1 & v_2 & \ldots & v_n 
\end{bmatrix}^T\in\mathbb{R}^n$ and  
$w=\begin{bmatrix}
          w_1 & w_2 & \ldots & w_n 
\end{bmatrix}^T\in\mathbb{R}^n$, then $v + w=\begin{bmatrix}
          v_1 + w_1 & v_2 + w_2 & \ldots & v_n + w_n 
\end{bmatrix}^T\in\mathbb{R}^n$. The so-called **parallelogram law** gives the rule for vector addition. For two vectors $u$ and $v$ represented by the adjacent sides (both in magnitude and direction) of a parallelogram drawn from a point, the vector sum $u+v$ is is represented by the diagonal of the parallelogram drawn from the same point:

<img src = "images/sum_of_vectors.png" width="230" align="middle"/>

In Python you can either use `+` operator or `NumPy` function `np.add()`.

#### Norm of a Vector

The norm of a vector $v$ is denoted as $\lvert v\rvert$. It is a nonnegative number that describes the extent of the vector in space (its length). The norm of a vector can be found using `NumPy` function `np.linalg.norm()`.

### Dot Product

The **dot product** (or **scalar product**) is an algebraic operation that takes two vectors $x=\begin{bmatrix}
          x_1 & x_2 & \ldots & x_n 
\end{bmatrix}^T\in\mathbb{R}^n$ and  
$y=\begin{bmatrix}
          y_1 & y_2 & \ldots & y_n 
\end{bmatrix}^T\in\mathbb{R}^n$ and returns a single scalar. The dot product can be represented with a dot operator $x\cdot y$ and defined as:

$$x\cdot y = \sum_{i=1}^{n} x_iy_i = x_1y_1+x_2y_2+\ldots+x_ny_n \tag{1}$$

#### Dot product using Python 
The simplest way to calculate dot product in Python is to take the sum of element by element multiplications. You can define the vectors $x$ and $y$ by listing their coordinates. 

Dot product is very a commonly used operator, so `NumPy` linear algebra package provides quick way to calculate it using function `np.dot()`.

Note that you did not have to define vectors $x$ and $y$ as `NumPy` arrays, the function worked even with the lists. But there are alternative functions in Python, such as explicit operator `@` for the dot product, which can be applied only to the `NumPy` arrays. You can run the following cell to check that.

As both `np.dot()` and `@` operators are commonly used, it is recommended to define vectors as `NumPy` arrays to avoid errors.

#### Speed of Calculations in Vectorized Form

Dot product operations in Machine Learning applications are applied to the large vectors with hundreds or thousands of coordinates (called **high dimensional vectors**). Training models based on large datasets often takes hours and days even on powerful machines. Speed of calculations is crucial for the training and deployment of your models. 

It is important to understand the difference in the speed of calculations using vectorized and the loop forms of the vectors and functions. In the loop form operations are performed one by one, while in the vectorized form they can be performed in parallel. In the section above you defined loop version of the dot product calculation (function `dot()`), while `np.dot()` and `@` are the functions representing vectorized form.

Vectorization is extremely beneficial in terms of the speed of calculations!

#### Geometric Definition of the Dot Product

In [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space), a Euclidean vector has both magnitude and direction. The dot product of two vectors $x$ and $y$ is defined by:

$$x\cdot y = \lvert x\rvert \lvert y\rvert \cos(\theta),\tag{2}$$

where $\theta$ is the angle between the two vectors:

<img src = "images/dot_product_geometric.png" width="230" align="middle"/>

This provides an easy way to test the orthogonality between vectors. If $x$ and $y$ are orthogonal (the angle between vectors is $90^{\circ}$), then since $\cos(90^{\circ})=0$, it implies that **the dot product of any two orthogonal vectors must be $0$**. Let's test it, taking two vectors $i$ and $j$ we know are orthogonal.

#### Application of the Dot Product: Vector Similarity

Geometric definition of a dot product is used in one of the applications - to evaluate **vector similarity**. In Natural Language Processing (NLP) words or phrases from vocabulary are mapped to a corresponding vector of real numbers. Similarity between two vectors can be defined as a cosine of the angle between them. When they point in the same direction, their similarity is 1 and it decreases with the increase of the angle. 

Then equation $(2)$ can be rearranged to evaluate cosine of the angle between vectors:

$\cos(\theta)=\frac{x \cdot y}{\lvert x\rvert \lvert y\rvert}.\tag{3}$

Zero value corresponds to the zero similarity between vectors (and words corresponding to those vectors). Largest value is when vectors point in the same direction, lowest value is when vectors point in the opposite directions.

This example of vector similarity is given to link the material with the Machine Learning applications. There will be no actual implementation of it in this Course. Some examples of implementation can be found in the Natual Language Processing Specialization.

