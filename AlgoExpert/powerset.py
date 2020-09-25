# Given an array input, return all powersets (combinations including empty set
# and the array itself)

# Iterative Solution
# Complexity O(n * 2^n) Time and Space
def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets

# Recursive Solution
# Complexity O(n * 2^n) Time and Space
# def powerset(array, idx = None):
#     if idx is None:
#         idx = len(array) - 1
#     if idx < 0:
#         return [[]]
#     ele = array[idx]
#     subsets = powerset(array, idx - 1)
#     for i in range(len(subsets)):
#         currentSubset = subsets[i]
#         subsets.append(currentSubset + [ele])
#     return subsets