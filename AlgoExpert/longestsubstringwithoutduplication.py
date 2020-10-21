'''
Given an input string, return the longest substring not containing duplicate characters 
within the string.
'''

# Complexity - O(N) Time | O(min(N, A)) Space
# Where N is the length of the given string, and A is the unique letters in the
# given string.
def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if i + 1 - startIdx > longest[1] - longest[0]:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]