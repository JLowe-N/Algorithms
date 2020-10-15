'''
Given a list of test scores, you need to give the students rewards based on the scores.
The rules you want to follow for rewards are as follows:
    1. Every student must get at least 1 reward.
    2. If a student has greater score than a neighbor, then they should get more
    rewards than that neighbor.
    3. If a student has a lesser score than a neighbor, then they should get less
    rewards than that neighbor.

Notes:
The supplied list will not necessarily be sorted.
The scores are positive integers and are all unique.
'''
# Optimal Solution - Iterate from left, then iterate from the right, incrementing
# rewards as needed
# Complexity - O(N) Time | O(N) Space where N is the number of scores in the list
def minRewards(scores):
    rewards = [1 for score in scores]
    for i in range(0, len(scores) - 1):
        if scores[i + 1] > scores[i]:
            rewards[i + 1] = rewards[i] + 1
    for i in reversed(range(1, len(scores))):
        if scores[i - 1] > scores[i]:
            rewards[i - 1] = max(rewards[i - 1], rewards[i] + 1)
    return sum(rewards)

# Solution #2 - Find local mins, then iterate out left and right, incrementing rewards
# until a peak is reached.  O(N) time, space, but less readable code

# def minRewards(scores):
#     rewards = [1 for _ in scores]
#     localMinIdxs = getLocalMinIdxs(scores)
#     for localMinIdx in localMinIdxs:
#         expandFromLocalMins(localMinIdx, scores, rewards)
#     return sum(rewards)
    
# def expandFromLocalMins(localMinIdx, scores, rewards):
#     leftIdx = localMinIdx - 1
#     while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
#         rewards[leftIdx] = max(rewards[leftIdx + 1] + 1, rewards[leftIdx])
#         leftIdx -= 1
#     rightIdx = localMinIdx + 1
#     while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
#         rewards[rightIdx] = rewards[rightIdx - 1] + 1
#         rightIdx += 1
#     return

# def getLocalMinIdxs(array):
#     if len(array) == 1:
#         return [0]
#     localMinIdxs = []
#     for i in range(len(array)):
#         if i == 0 and array[0] < array[1]:
#             localMinIdxs.append(i)
#         elif i == len(array) - 1 and array[-1] < array[-2]:
#             localMinIdxs.append(i)
#         elif i == 0 or i == len(array) - 1:
#             continue
#         elif array[i - 1] > array[i] and array[i + 1] > array[i]:
#             localMinIdxs.append(i)
#     return localMinIdxs


# Solution #3 - Naive solution - increment rewards in array, but if a new min
# found, backtrack and correct rewards array - Complexity O(N^2) time | O(N) space

# def minRewards(scores):
#     rewards = [1 for score in scores]
#     for i in range(1, len(scores)):
#         j = i - 1
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j] + 1
#         else:
#             while j >= 0 and scores[j] > scores[j + 1]:
#                 rewards[j] = max(rewards[j], rewards[j + 1] + 1)
#                 j -= 1
#     return sum(rewards)


