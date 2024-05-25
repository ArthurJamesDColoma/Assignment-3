import numpy as np

# 1. Save and Writing Files using numpy

# Example 1: Saving an array to a text file
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('array1.txt', array1, delimiter=',')

# Example 2: Saving an array to a binary .npy file
array2 = np.array([1.5, 2.5, 3.5, 4.5])
np.save('array2.npy', array2)

# Example 3: Saving multiple arrays to a compressed .npz file
array3_1 = np.array([1, 2, 3])
array3_2 = np.array([4, 5, 6])
np.savez_compressed('arrays.npz', array3_1=array3_1, array3_2=array3_2)

print("----------------------")

# 2. Load data from Files using numpy

# Example 1: Loading an array from a text file
loaded_array1 = np.loadtxt('array1.txt', delimiter=',')
print("Array loaded from text file:")
print(loaded_array1)

# Example 2: Loading an array from a binary .npy file
loaded_array2 = np.load('array2.npy')
print("\nArray loaded from .npy file:")
print(loaded_array2)

# Example 3: Loading multiple arrays from a compressed .npz file
loaded_arrays = np.load('arrays.npz')
loaded_array3_1 = loaded_arrays['array3_1']
loaded_array3_2 = loaded_arrays['array3_2']
print("\nArrays loaded from .npz file:")
print("First array:")
print(loaded_array3_1)
print("Second array:")
print(loaded_array3_2)