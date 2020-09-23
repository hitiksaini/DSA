# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)

# Complexity
# Since radix sort is a non-comparative algorithm, it has advantages over comparative sorting algorithms.

# For the radix sort that uses counting sort as an intermediate stable sort, the time complexity is O(d(n+k)).

# Here, d is the number cycle and O(n+k) is the time complexity of counting sort.

# Thus, radix sort has linear time complexity which is better than O(nlog n) of comparative sorting algorithms.

# If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in linear time however the intermediate sort takes large space.

# This makes radix sort space inefficient. This is the reason why this sort is not used in software libraries.
