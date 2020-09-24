# Write a function that takes in an array of unique integers and returns an
# array of all permutations of those integers in no particular order
# If the input array is empty, return an empty array

# Complexity O(n * n!) Time, O(n * n!) Space
def getPermutations(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations

def permutationHelper(i,array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationHelper(i + 1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Complexity: Upper Bound O(n^2 * n!) Time  - but roughly O(n * n!)
# O(n * n!) Space
# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)
#     return permutations

# def permutationHelper(array, currentPermutation, permutations):
#     if not len(array) and len(currentPermutation):
#         permutations.append(currentPermutation)
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:] # O(n)
#             newPermutation = currentPermutation + [[array[i]]] # O(n)
#             permutationHelper(newArray, newPermutation, permutations)
