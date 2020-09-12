def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = [88, 45, 22, 81, 20, 19, 76]
size = len(data)
selectionSort(data, size)
print('Sorted Array :')
print(data)

# Number of comparisons: (n - 1) + (n - 2) + (n - 3) + ..... + 1 = n(n - 1) / 2 nearly equals to n^2.

# Complexity = O(n^2)

# Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity is n*n = n2.

# Time Complexities:

# Worst Case Complexity: O(n^2)
# If we want to sort in ascending order and the array is in descending order then, the worst case occurs.

# Best Case Complexity: O(n^2)
# It occurs when the array is already sorted

# Average Case Complexity: O(n^2)
# It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

# The time complexity of the selection sort is the same in all cases. At every step, you have to find the minimum element 
# and put it in the right place. The minimum element is not known until the end of the array is not reached.

# Space Complexity:

# Space complexity is O(1) because an extra variable is used.
