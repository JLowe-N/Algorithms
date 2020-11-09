'''
Function that takes in a non-negative integer n, and returns the number of possible
Binary Tree topologies that can be created with exactly n nodes.
A binary tree topology is defined as any Binary Tree configuration, irrespective of node values.

If n == 0, then there is only 1 topology - just a None / null node.
'''
# Solution 3 - Iteration with Cache
# Complexity O(N^2) Time | O(N) space
# where n is the number of nodes
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]
    

# Solution 2 - Recursion with Cache
# Complexity O(N^2) Time | O(N) space
# where n is the number of nodes
# def numberOfBinaryTreeTopologies(n, cache={0: 1}):
#     if n in cache:
#         return cache[n]
#     numberOfTrees = 0
#     for leftTreeSize in range(n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
#         numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
#         numberOfTrees += numberOfLeftTrees * numberOfRightTrees
#     cache[n] = numberOfTrees
#     return numberOfTrees


# Solution 1 - Naive Recursion / No Cache
# Complexity - Catalan Formula Upper Bound
# O( (n*(2n)!) / (n!(n + 1)!) ) Time | O(n) Space
# def numberOfBinaryTreeTopologies(n):
#     if n == 0:
#         return 1
#     numberOfTrees = 0
#     for leftTreeSize in range(n):
#         rightTreeSize = n - 1 - leftTreeSize
#         numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
#         numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
#         numberOfTrees += numberOfLeftTrees * numberOfRightTrees
#     return numberOfTrees
