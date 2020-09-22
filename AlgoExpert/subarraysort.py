# Given an array, return the indexes of the smallest subarray that can be
# sorted to sort the overall array.

def subarraySort(array):
    subarrayIdx = [-1, -1]
    smallestUnsorted = float("inf")
    largestUnsorted = float("-inf")
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            if array[i + 1] < smallestUnsorted:
                smallestUnsorted = array[i + 1]
            if array[i] < smallestUnsorted:
                smallestUnsorted = array[i]
        if array[i + 1] < array[i]:
            if array[i + 1] > largestUnsorted:
                largestUnsorted = array[i + 1]
            if array[i] > largestUnsorted:
                largestUnsorted = array[i]
    for i in range(len(array)):
        if array[i] > smallestUnsorted and subarrayIdx[0] == -1:
            subarrayIdx[0] =  i
        if array[len(array) - 1 - i] < largestUnsorted and subarrayIdx[1] == -1:
            subarrayIdx[1] = len(array) - 1 - i
    return subarrayIdx
