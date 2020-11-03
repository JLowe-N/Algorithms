'''
You wish to find an apartment with the shortest walk to all the feature requirements
on your amenities list (gym, store, pool, etc.)

Given a list of blocks, where each block element is a hash table of the features
at that given block and an array of requirements for that you wish to be close to,
return the ideal block which has the shortest maximum walk for all the requirements.

All blocks are contiguous and each index position is equidistance from the neighboring
indexes.
'''

# Solution 1 Iterate through each block for each requirement, then find the
# block with the minimum longest walk
# Complexity O(BR) time | O(BR) Space where B is # blocks and R is # reqs


def apartmentHunting(blocks, reqs):
    minDistancesFromBlocks = list(
        map(lambda req: getMinDistances(blocks, req), reqs))  # O(br) time
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(
        blocks, minDistancesFromBlocks)  # O(br) time
    return getIdxAtMinValue(maxDistancesAtBlocks)  # O(b) time


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for blocks in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(
            map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(
            minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances


def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a - b)


# Solution 2 Iterate through all blocks, all reqs, and again through all blocks
# to find the distance to each req
# Complexity O(B^2*R) time | O(B) space where B is # of blocks and R is # of reqs
# def apartmentHunting(blocks, reqs):
#     maxDistancesAtBlocks = [float("-inf") for block in blocks]
#     for i in range(len(blocks)):
#         for req in reqs:
#             closestReqDistance = float("inf")
#             for j in range(len(blocks)):
#                 if blocks[j][req]:
#                     closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
#             maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
#     return getIdxAtMinValue(maxDistancesAtBlocks)

# def getIdxAtMinValue(array):
#     idxAtMinValue = 0
#     minValue = float("inf")
#     for i in range(len(array)):
#         currentValue = array[i]
#         if currentValue < minValue:
#             minValue = currentValue
#             idxAtMinValue = i
#     return idxAtMinValue

# def distanceBetween(a, b):
#     return abs(a - b)
