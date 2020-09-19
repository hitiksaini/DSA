# Time Complexities

# Best case complexity: O(1)
# Average case complexity: O(log n)
# Worst case complexity: O(log n)
# Space Complexity

# The space complexity of the binary search is O(n).

# Iterative approach

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
    
 # recursive approach
#  un-comment the part to see recursive method
# recursive approach
# def binarySearch(array, x, low, high):
#     if high >= low:
#         mid = low + (high - low)//2
#         # If found at mid, then return it
#         if array[mid] == x:
#             return mid
#         # Search the left half
#         elif array[mid] > x:
#             return binarySearch(array, x, low, mid-1)
#         # Search the right half
#         else:
#             return binarySearch(array, x, mid + 1, high)
#     else:
#         return -1
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x, 0, len(array)-1)
# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")
