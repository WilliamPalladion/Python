import numpy as np
import matplotlib.pyplot as plt

# meshgrid function

m, n = (5, 3)
x = np.linspace(0, 1, m)
y = np.linspace(0, 1, n)

X, Y = np.meshgrid(x, y)
# note that the dimension for both array is n * m, not m * n!

print(X)
print(Y)

#plt.style.use('ggplot')
#plt.plot(X, Y, marker='.', color='blue', linestyle='none')
#plt.show()

# use zip command to get the grid point coordinates
z = [i for i in zip(X.flat, Y.flat)]  # flat means flatten the array into one row
print(z)

print('-------------------------------------------------')

points = np.arange(-5, 5, 0.01)  # 1000 equally-spaced nodes
xs, ys = np.meshgrid(points, points)  # or meshgrid(points), same effect
#print(xs)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
#plt.imshow(z, cmap='gray')
#plt.colorbar()
#plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
#plt.show()

print('--------------------------------------------------')


# Expressing conditional logic as array operations

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# if condition is true we take value from x, false for value in y

result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)

# this method will be slow when arrays are large and not works for high dimensional ones
# we can use np.where function

result = np.where(cond, xarr, yarr)
print(result)

# one application of this method is to rebuild the arrays
arr = np.random.randn(4, 4)
print(arr)

rebuild = np.where(arr > 0, 2, -2)
# all positive values become 2, while all negative values become -2
print(rebuild)

# or we can only change positive values, leaving others unchanged
rebuild = np.where(arr > 0, 2, arr)  # combine scalars and arrays

print('--------------------------------------------------')

# Statitical methods

arr = np.random.randn(5, 4)
print(arr)

print(arr.mean())
# or we use   np.mean(arr)
print(arr.mean(axis=0))  # column average
print(arr.mean(axis=1))  # row average

print(arr.sum())
print(arr.sum(axis=0))  # column sum
print(arr.sum(axis=1))  # row sum


# cumulative sum and product
arr = np.arange(8)
print(np.cumsum(arr))

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.cumprod())

# for high dimensions

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(arr1.cumsum(axis=0))  # add along columns
print(arr1.cumsum(axis=1))  # add along rows

print(arr1.cumprod(axis=0))  # multiply along columns
print(arr1.cumprod(axis=1))  # multiply along rows

print('------------------------------------------')

# for boolean arrays

arrb = np.random.randn(100)

cond_sum = (arrb > 0).sum()  # here sum computes how many positive values, not the arithmetic sum
print(cond_sum)

bools = np.array([True, False, True, False,True])
print(bools.any())  # returns True if any one is True
print(bools.all())  # returns True if all values are True

print('-------------------------------------------')


# Sorting

arr = np.random.randn(6)
arr.sort()   # sort is an operation on the original array!
print(arr)

# sorting for multi-dimensional arrays

arr = np.random.randn(5, 3)
print(arr)

#  arr.sort(axis=0)  # sort along columns
#  print(arr)

# But if we use the np.sort, it will produce a new array!

print(np.sort(arr, axis=0))  # along columns
print(arr)

# one method to compute quartiles
# first sort, then return its position as index

large_arr = np.random.randn(1000)
large_arr.sort()

# 5% quartile
p_quartile = large_arr[int(0.05 * len(large_arr))]
print(p_quartile)

print('-------------------------------------------')


# Unique and other set logic

# np.unique

names = np.array(['Joe', 'Bob', 'Tesla', 'Bob', 'Joe'])
print(np.unique(names))

# if use python codes
print(sorted(set(names)))

ints = np.array([1, 1, 2, 2, 2, 3, 3, 4])

print(np.unique(ints))

# np.in1d, test whether one value in an array is in another array

print(np.in1d(ints, [1, 5, 6]))

