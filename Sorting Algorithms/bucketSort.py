def bucketSort(array):
    bucket = []
    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])
    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array
array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))

# Complexity
# Worst Case Complexity: O(n^2)
# When there are elements of close range in the array, they are likely to be placed in the same bucket. 
# This may result in some buckets having more number of elements than others.
# It makes the complexity depend on the sorting algorithm used to sort the elements of the bucket.
# The complexity becomes even worse when the elements are in reverse order. If insertion sort is used to sort elements of the bucket, then the time complexity becomes O(n2).
# Best Case Complexity: O(n+k)
# It occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each bucket.
# The complexity becomes even better if the elements inside the buckets are already sorted.
# If insertion sort is used to sort elements of a bucket then the overall complexity in the best case will be linear ie. O(n+k). O(n) 
# is the complexity for making the buckets and O(k) is the complexity for sorting the elements of the bucket using algorithms having linear time complexity at the best case.
# Average Case Complexity: O(n)
# It occurs when the elements are distributed randomly in the array. Even if the elements are not distributed uniformly, bucket sort runs in linear time. 
# It holds true until the sum of the squares of the bucket sizes is linear in the total number of elements.
