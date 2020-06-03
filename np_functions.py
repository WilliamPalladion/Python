import numpy as np

arr = np.arange(10)
print(arr)

# element-wise functions (unary ufuncs)

print(np.sqrt(arr))
print(np.exp(arr))

np.power(arr, 2)   # arr ** 2

arr1 = np.arange(20)
np.power(arr, 2, out=arr1[:10])   # use output to fill the first 10 numbers in arr1

print('------------------------------------------')
# binary ufucs

x = np.random.randn(8)
y = np.random.randn(8)

print(x)
print(y)

print(np.maximum(x, y))

np.add(x, y)  # x + y, even if they differ in range, it will be broadcast
np.subtract(x, y)  # x - y

# use out parameter
z = np.empty(8)
np.multiply(x, y, out=z)


print('------------------------------------------')

# integer division
print(100 // 21)  # 4, quotient
print(5 % 3)   # 2, remainder

# function modf

# for a, b are both integers, it will return ( a//b, a%b )
# for a, b are floating numbers, it returns (math.floor(a/b), a%b)

arr = np.random.randn(7) * 5
print(arr)

remainder, whole_part = np.modf(arr)
# return integer and decimal parts as separate arrays

print(remainder)
print(whole_part)

print('---------------------------------------------')

#  some Unary functions
np.abs()
np.sqrt()
np.square()
np.exp()
np.log()
np.log10()

np.sign()
np.ceil()
np.floor()
np.rint()  # round to the nearest integer

np.isnan()   # return boolean value if each number is NaN
np.isfinite()
np.isinf()

np.std()
np.var()
np.median()  # axis = 0 = column
np.mean()
np.max()
np.min()

np.argmax()  # return indices of maximum
np.argmin()
np.argsort()

# binary universal functions
np.greater()
np.greater_equal()  # return boolean value
np.less()
np.less_equal()
np.equal()
np.not_equal()

np.logical_and(x > 4, x < 8)
np.logical_not()
np.logical_or()
np.logical_xor()



