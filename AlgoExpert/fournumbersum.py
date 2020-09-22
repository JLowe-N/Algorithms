# Given an array and a target sum, return all quadruplets that add up 
# to the target sum in a two-dimensional array.

# array = [7, 6, 4, -1, 1, 2]
# targetSum = 16
# result: [[7, 6, 4, -1], [7, 6, 1, 2]]

def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        # iterate forward from i, looking for matching pairs in hash table
        # then iterate backward from i adding new sums to hash table
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets
    