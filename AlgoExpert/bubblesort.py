# Ascending Version: Iterate through the array, checking if current element is
# larger than the next element.  If so, array is not sorted and elements are
# swapped.  The current iteration through the array is continued, and we will 
# need to keep iterating through the array until all the element comparisons
# are correct.  At the end of each iteration, the largest element will bubble
# up so we will need to check one less element per run.

# Time Complexity O(N^2) because we need to run through the array multiple times
# making comparisons against each element - Worst and Average Case
# Space Complexity O(1) - no additional space usage proportional to the input size,
# so constant space.

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(array, i, i+ 1)
                isSorted = False
        counter += 1
    return array
              
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
