'''
Function that returns True if given strings one and two can be interwoven
to create string three.  Interweaving means that the strings are merged by
aleternating their letters without any specific pattern.  Letters within a
string must maintain their relative ordering in the interwoven string.

The interwoven string must be an exact match to string three - no missing or extra
letters.
'''

# Solution 2 - Cache
# Complexity O(nm) Time | O(nm) space
# Where n and m are the lengths of strings one and two


def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False

# Solution 1 - Naive Recursive (no cache)
# Complexity O(2^(n + m)) Time O(n + m) Space
# def interweavingStrings(one, two, three):
# 	return areInterwoven(one, two, three, 0, 0)

# def areInterwoven(one, two, three, i, j):
#     k = i + j
#     if k == len(three) and i == len(one) and j == len(two):
#         return True
#     elif k == len(three) and (i != len(one) or j != len(two)):
#         return False

#     oneTest, twoTest = (False, False)
#     if i < len(one) and one[i] == three[k]:
#         oneTest = areInterwoven(one, two, three, i + 1, j)
#     if j < len(two) and two[j] == three[k]:
#         twoTest = areInterwoven(one, two, three, i, j + 1)
#     return oneTest or twoTest
