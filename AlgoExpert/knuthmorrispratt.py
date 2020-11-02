
'''
Given a string and a substring, returns a bool indicating if the substring
is contained in the string.
'''
# KMP Solution
# Complexity O(N + M) time | O(M) space
# Where N is length of string and M is length of smaller substring
# M space used to store pattern array on substring
def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    return doesMatch(string, substring, pattern)

# O(M) Time | O(M) Space
def buildPattern(substring):
    pattern = [-1 for i in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern

# O(N) Time
def doesMatch(string, substring, pattern):
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False


# Brute Force Solution
# Complexity O(N * M) Time O(1) Space where N is string len and M is substring len
# def knuthMorrisPrattAlgorithm(string, substring):
#     currentLetter = 0
#     j = 0
#     while currentLetter < len(string) and j < len(substring):
#         i = currentLetter
#         j = 0
#         for j in range(len(substring)):
#             if string[i] == substring[j]:
#                 i += 1
#                 j += 1
#             else:
#                 currentLetter += 1
#                 break
#     return j == len(substring)
