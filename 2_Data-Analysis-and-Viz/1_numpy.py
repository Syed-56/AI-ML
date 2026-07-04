import numpy as np

#creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1, type(arr1), arr1.shape, "\n")   # (5,)  <- 1D, note the trailing comma

#2D Array
arr2 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2, arr2.shape, "\n")   # (2, 5) -> 2 rows, 5 cols

#Handy Methods to construct an array
print(np.arange(0, 10, 2, dtype=int), "\n")     # [0,2,4,6,8]  -> start at 0, stop at 10, step is 2
print(np.ones((3,4), dtype=int), "\n")          # 3x4 array of 1.0
print(np.zeros((2,2), dtype=int), "\n")          # 2x2 array of 0.0
print(np.eye(3, 2), "\n")             # identity matrix like array, 3 rows 2 cols
print(np.linspace(0, 15, 5), "\n")     # 5 evenly spaced numbers between 0 and 15

#Attributes
print(arr2.ndim)       # number of dimensions
print(arr2.size)      # total element count
print(arr2.dtype)      # data type (int32/int64 depending on OS)
print(arr2.itemsize)   # bytes per element

#Vectorized Operations
r1 = np.array([1,2,3,4,5])
r2 = np.array([10,20,30,40,50])

sum = r1 + r2   # element-wise: [11,22,33,44,55]
sub = r1 - r2
prod = r1 * r2
div = r1 / r2
print(sum,sub,prod,div, "\n")

#Universal Operations
sqrt_arr = np.sqrt(arr1)
exp_arr = np.exp(arr1)
sin_arr = np.sin(arr1)
log_arr = np.log(arr1)
print(sqrt_arr)
print(exp_arr)
print(sin_arr)
print(log_arr, "\n")

#Indexing/Slicing
arr = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

arr[0, 0]        # 1        -> row 0, col 0
arr[1:, 2:]       # [[7,8],[11,12]]   -> rows from 1 onward, cols from 2 onward
arr[1:3, 1:3]     # [[6,7],[10,11]]

#Boolean Masking
data = np.arange(1, 11)
mask = data > 5          # array of True/False
data[mask]                # [6,7,8,9,10]
# combine conditions — must use & / | with parentheses, not "and"/"or"
data[(data > 5) & (data < 8)]   # [6,7]

#Stats
np.mean(arr1)
np.median(arr1)
np.std(arr1)     # standard deviation
np.var(arr1)      # variance
normalized = (data - np.mean(data)) / np.std(data)