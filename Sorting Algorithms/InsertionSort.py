def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1     
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array :')
print(data)

# Time Complexities

# Worst Case Complexity: O(n^2)
# Suppose, an array is in ascending order, and you want to sort it in descending order. In this case,
# worst case complexity occurs.

# Each element has to be compared with each of the other elements so, for every nth element,(n-1) number of comparisonsare made.

# Thus, the total number of comparisons = n*(n-1) ~ n^2

# Best Case Complexity: O(n)
# When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all.
# So, there are only n number of comparisons. Thus, complexity is linear.

# Average Case Complexity: O(n2)
# It occurs when the elements of an array are in jumbled order (neither ascending nor descending).

# Space Complexity
# Space complexity is O(1) because an extra variable key is used.
