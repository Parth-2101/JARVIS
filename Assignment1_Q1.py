import numpy as np

array = np.random.randint(1, 101, size=(5, 5))
print("Original Array:")
print(array)

middle_element = array[2, 2]
print("\nMiddle Element:", middle_element)

row_means = np.mean(array, axis=1)
print("\nMean of Each Row:", row_means)

overall_mean = np.mean(array)
greater_than_mean = array[array > overall_mean]
print("\nElements Greater than Overall Mean:", greater_than_mean)

def spiral(matrix):
    n = matrix.shape[0]
    for i in range((n + 1) // 2):
        for a in range(i, n - i):
            print(matrix[i, a], end=" ")
        for a in range(i + 1, n - i):
            print(matrix[a, n - 1 - i], end=" ")
        for a in range(i + 1, n - i):
            print(matrix[n - 1 - i, n - 1 - a], end=" ")
        for a in range(i + 1, n - 1 - i):
            print(matrix[n - 1 - a, i], end=" ")

print("\n\nSpiral Traversal:")
spiral(array)
