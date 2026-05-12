## Numpy Arrays

### Advantages of using NumPy arrays

Arrays are one of the core data structures of the NumPy library, essential for organizing your data. You can think of them as a grid of values, all of the same type. If you have used Python lists before, you may remember that they are convenient, as you can store different data types. However, Python lists are limited in functions and take up more space and time to process than NumPy arrays.

NumPy provides an array object that is much faster and more compact than Python lists. Through its extensive API integration, the library offers many built-in functions that make computing much easier with only a few lines of code. This can be a huge advantage when performing math operations on large datasets. 

The array object in NumPy is called `ndarray` meaning 'n-dimensional array'. To begin with, you will use one of the most common array types: the one-dimensional array ('1-D'). A 1-D array represents a standard list of values entirely in one dimension. Remember that in NumPy, all of the elements within the array are of the same type.

### How to create NumPy arrays

There are several ways to create an array in NumPy. You can create a 1-D array by simply using the function array() which takes in a list of values as an argument and returns a 1-D array.

Another way to implement an array is using `np.arange()`. This function will return an array of evenly spaced values within a given interval. To learn more about the arguments that this function takes, there is a powerful feature in Jupyter Notebook that allows you to access the documentation of any function by simply pressing `shift+tab` on your keyboard when clicking on the function. Give it a try for the built-in documentation of `np.arange()`.

What if you wanted to create an array with five evenly spaced values in the interval from 0 to 100? As you may notice, you have 3 parameters that a function must take. One parameter is the starting number, in this case 0, the final number 100 and the number of elements in the array, in this case, 5. NumPy has a function that allows you to do specifically this by using `np.linspace()`.

Did you notice that the output of the function is presented in the float value form (e.g. "... 25. 50. ...")? The reason is that the default type for values in the NumPy function `np.linspace` is a floating point `(np.float64)`. You can easily specify your data type using `dtype`. If you access the built-in documentation for the functions, you will notice that most Numpy functions take an optional parameter `dtype`. In addition to float, NumPy has several other data types such as `int`, and `char`.

To change the type to integers, you need to set the `dtype` to `int`. You can do so, even in the previous functions. 

### More on Numpy Arrays

One of the advantages of using NumPy is that you can easily create arrays with built-in functions such as:

- `np.ones()` - Returns a new array setting values to one.
- `np.zeros()` - Returns a new array setting values to zero.
- `np.empty()` - Returns a new uninitialized array.
- `np.random.rand()` - Returns a new array with values chosen at random.

### Multidimensional Arrays

With NumPy you can also create arrays with more than one dimension. In the above examples, you dealt with 1-D arrays, where you can access their elements using a single index. A multidimensional array has more than one column. Think of a multidimensional array as an excel sheet where each row/column represents a dimension.

An alternative way to create a multidimensional array is by reshaping the initial 1-D array. Using `np.reshape()` you can rearrange elements of the previous array into a new shape.

#### Finding size, shape and dimension
These are all atrributes of a `ndarray` and can be accessed as follows:

- `ndarray.ndim` - Stores the number dimensions of the array.
- `ndarray.shape` - Stores the shape of the array. Each number in the tuple denotes the lengths of each corresponding dimension.
- `ndarray.size` - Stores the number of elements in the array.

### Array math operations

NumPy allows you to quickly perform elementwise addition, substraction, multiplication and division for both 1-D and multidimensional arrays. The operations are performed using the math symbol for each '+', '-' and '*'. Recall that addition of Python lists works completely differently as it would append the lists, thus making a longer list, in addition, subtraction and multiplication of Python lists do not work.

#### Multiplying vector with a scalar (broadcasting)

Suppose you need to convert miles to kilometers. To do so, you can use the NumPy array functions that you've learned so far. You can do this by carrying out an operation between an array (miles) and a single number (the conversion rate which is a scalar). Since, 1 mile = 1.6 km, NumPy computes each multiplication within each cell.

This concept is called **broadcasting**, which allows you to perform operations specifically on arrays of different shapes.

### Indexing and slicing
Indexing is very useful as it allows you to select specific elements from an array. It also lets you select entire rows/columns or planes as you'll see in future assignments for multidimensional arrays.

#### a. Indexing
Let us select specific elements from the arrays as given.

e.g: `print(a[0])`

For multidimensional arrays of shape `n`, to index a specific element, you must input `n` indices, one for each dimension.

#### b. Slicing
Slicing gives you a sublist of elements that you specify from the array. The slice notation specifies a start and end value, and copies the list from start up to but not including the end (end-exclusive).

The syntax is:

`array[start:end:step]`

If no value is passed to start, it is assumed `start = 0`, if no value is passed for end, it is assumed that `end = length of array` and if no value is passed to step, it is assumed `step = 1`.

### Stacking
Finally, stacking is a feature of NumPy that leads to increased customization of arrays. It means to join two or more arrays, either horizontally or vertically, meaning that it is done along a new axis.

- `np.vstack()` - stacks vertically
- `np.hstack()` - stacks horizontally
- `np.hsplit()` - splits an array into several smaller arrays


