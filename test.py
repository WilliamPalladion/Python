import numpy as np

x = np.logspace(0, 3, 10, base=2)

arr = np.arange(10)
arr1 = np.zeros(20, dtype=np.int)

np.power(arr, 2, out=arr1[:10])

print(arr1)