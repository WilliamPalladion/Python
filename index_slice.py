import numpy as np

# generate some random data

data = np.random.rand(2, 3)
data = np.random.randn(2, 3)  # random normal
data = np.random.randint(low=0, high=20, size=(2, 3))  # [0, 20), random integers

data = np.random.normal(loc=5, scale=10, size=(2, 3))  # expectation = 5, variance = 10

print(data)
print(data.shape[0])
print(data.dtype)

arr = np.linspace(0, 10, 1)  # equally spaced, arithmetic progression
arr = np.logspace(1, 10, num=20, base=2)
# geometric progression, (2^1, ..., 2^2, ..., 2^10) with equally 20 spaced nodes


# generate n-dimensional arrays

data1 = [[1, 2, 3], [3, 4, 5]]

arr1 = np.array(data1)

print(arr1)
print(arr1.shape)
print(arr1.ndim)
print(arr1.dtype)

arr2 = np.zeros((3, 2))
print(arr2)

arr3 = np.empty((2, 3, 2))
print(arr3)

print(np.arange(10))

print(np.ones((2, 1)))
print(np.ones_like(arr2))  # print all 1 array with same shape and dtype of another array

print(np.full((2, 3), 4))
print(np.full_like(arr2, 5))  # fit in with indicated value

print(np.eye(3))
print(np.identity(4))  # identity matrix (ndarray)




# Data types in ndarray

arr4 = np.array([1, 2, 3], dtype=np.int32)
print(arr4.dtype)

# change type of data by command astype

float_arr = arr4.astype(np.float64)
print(float_arr.dtype)

# if change float to int, number after decimal places will lost;

arr = np.array([1.2, 3.2, 4.5])
arr_change = arr.astype(np.int32)
print(arr_change)

# change numbers in string to numeric ones

numeric_string = np.array(['2.3', '3.45', '4.52'], dtype=np.string_)
print(numeric_string)
print(numeric_string.astype(np.float))

# we can also use other arrays type to assign
print(numeric_string.astype(float_arr.dtype))

# use abbreviations

zero_uint32 = np.zeros(4, dtype='u4')
print(zero_uint32)


print('----------------------------------------')
# Arithmetic operations with ndarray

arr = np.array([[1, 2, 3], [4, 5, 6]])

# element_wise

print(arr * arr)
print(arr - arr)
print(arr * 0.5)
print(arr ** 0.5)  # power, using two stars **
print(1 / arr)

arr1 = np. array([[0, 4, 1], [3, 7, 9]])
print(arr1 > arr)  # output a boolean array


# indexing and slicing

# 1-dimension
arr = np.arange(10)
print(arr)
print(arr[5])  # index starts from 0
print(arr[1:4])  # left-closed and right-open [1,4)
print(arr[:3])   # right-open [0, 3)

arr[1:4] = 12
print(arr)
print(arr[:])

# one main difference is that when we change the slice, the original array will change
# while the list built in Python will create a new one, not affecting original one

arr_slice = arr[5:8]  # arr_slice = [ 5, 6, 7 ]
arr_slice[1] = 125  # note the index
print(arr)

# we can understand the slice in ndarray is just a 'view' of the original one,
# not creating a new array

print('Use copy() command to create a new one')

arr_copy = arr[5:8].copy()
print(arr_copy)

arr_copy[1] = 200
print(arr_copy)
print(arr)  # original array does not change


# 2-dimensional

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[2])  # [7, 8, 9] single index represents the 1d array
print(arr2d[0, 2])
print(arr2d[1][1])  # index a single number

print(arr2d[:2, 1:])  # row[0,2), line[1:N]
print(arr2d[:, 1])   # second line

# higher dimensional (>=3d)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

print(arr3d)  # 2*2*3 array


print(arr3d[0])  # single index returns 2*3 array in pages

# scalars and arrays all can be assigned

print('------------------------------------------')
old_values = arr3d[0].copy()
arr3d[0] = 40
print(arr3d[0])

# assign arrays
arr3d[0] = old_values
print(arr3d[0])

print('------------------------------------------')


# double & triple indexes

print(arr3d[1, 0])  # index follows [ page, row, line ]
print(arr3d[1, 0, 2])

print(arr3d[:1, :, 1:])  # page 1, line 2 & 3
# All these slicing are just views!! Changes to them will affect the original array

print('-----------------------------------------')

# Boolean indexing
print()

names = np.array(['Bob', 'James', 'Jack', 'Bob', 'Sam'])
data = np.random.randn(5, 4)
print(data)
print(names == 'Bob')

print('indexing using boolean operators')
print('data[ names == \'Bob\']:')

# row index correspond to when boolean value is true
print(data[names == 'Bob'])
print(data[names == 'Bob', 1:])

# use != or ~ operator to represent opposite conditions

print(names != 'Bob')
print(data[~(names == 'Bob')])

# or we can name a condition as a variable
cond = names == 'Bob'
print(data[~cond, 2:])

# combine several boolean conditions ( &  or | )

cond1 = (names == 'Bob') | (names == 'Jack')
boo_slice = data[cond1]

boo_slice[boo_slice < 0] = 0   # modify values
print(boo_slice)
print(data)

# One interesting point is that boolean slice produces a new array,
# which means changing the slice will not change the original array,
# different from other indexing methods.

data[names != 'Bob'] = 10
print(data)

print('---------------------------------------------')

# Fancy indexing
print()

arr = np.empty((4, 4))

line = arr.shape[0]

for i in range(line):
    arr[i] = i

print(arr)

# select several lines by list of integers
print(arr[[1, 3]])
print(arr[[-1, -3]])  # inverse selection

# reshape arrays
arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])  # using tuples to index particular numbers

print()
print('Slice rectangular area')
print(arr[[1, 3, 7, 2]][:, [0, 3, 1, 2]])
# note this code arr[] [], means first choose line[1, 3, 7, 2]
# for this sliced array,then choose all the rows :, but for the lines,
# choose in the order [0, 3, 1, 2]

#  Note for fancy indexing, it also obtains a new array
print('--------------------------------------------------')


# Reshape arrays

a = np.random.randint(0, 10, size=(2, 4, 2))
a.reshape(shape=(4, 4))
a.reshape(16)
a.reshape(-1)  # change to 1-dimension

# other functions to change to 1-dimension
a.ravel()
a.flatten()


# Combine arrays

a = np.random.randn(2, 2)
b = np.random.randn(2, 2)

# horizontal & vertical combination

h_combine = np.hstack(a, b)  # [a, b]

v_combine = np.vstack(a, b)  # vertical combination

combine = np.concatenate(a, b, axis=0)  # axis = 0 = vstack(default), axis = 1 = hstack

# For 3d arrays, axis=0, 1, 2, now 0 = page, 1 = vstack, 2 = hstack


# Split arrays

a = np.arange(1, 9)  # [1, 2, 3, 4, 5, 6, 7, 8]

splines = np.split(a, 4)  # split into 4 arrays, can be called by splines[i], i= 0, 1, 2, 3
splines = np.split(a, [4, 6])  # 3 groups, indices 0123, indices 45, indices 6,..,N
# [1, 2, 3, 4]  [5, 6] [7, 8]

# split 2d arrays

a = np.random.randn(4, 4)

sp1, sp2 = np.split(a, 2, axis=0)  # horizontally split into two arrays
sp1, sp2, sp3 = np.split(a, [2, 3], axis=0)  # index 3 sections

sp1, sp2 = np.split(a, 2, axis=1)  # vertically split into 2 arrays


# hsplit & vsplit

sp1, sp2 = np.hsplit(a, 2)
sp1, sp2 = np.vsplit(a, 2)

sp = np.hsplit(a, [1, 2])



# Transpose and swap axes
# only returns a view, not inventing a new array

arr = np.array(range(15)).reshape((3, 5))

print(arr)
print(arr.T)  # .T  affix
print(arr.transpose())
# matrix product using np.dot

product_arr = np.dot(arr, arr.T)
print(product_arr)

# change axes
print('-------------------------------------')
arr = np.array(range(16)).reshape((2, 4, 2))
print(arr)

print(arr.transpose((1, 0, 2)))
# second axis become first, first become second, last not change i.e.(4, 2, 2)
# default transpose is   (i, j, k)  --->   (k, j, i)


print(arr.swapaxes(1, 2))  # swap first and second axis i.e.(2, 2, 4)

