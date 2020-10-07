# Given a big string to search, and a list of small strings to search for, 
# return an array of booleans that represent if the small string at that index
# is present in the big string.  Small string will not be longer than the big string.
# 
# Trie of all small strings
# O(ns + bs) time | O(ns) space
# where n is number of small strings, s is length of longest substring
# b is the big string length
# Time ns for building the smallStrings trie, bs for comparing big string to small string
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = string
    

# Special Suffix Trie from bigString
# O(b^2 + ns) Time | O(b^2 + n) Space
# Where b is the big string length, n is the number of small strings, s is the longest small string
# def multiStringSearch(bigString, smallStrings):
#     modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
#     return [modifiedSuffixTrie.contains(string) for string in smallStrings]
# class ModifiedSuffixTrie:
#     def __init__(self, string):
#         self.root = {}
#         self.populateModifiedSuffixTrieFrom(string)
    
#     def populateModifiedSuffixTrieFrom(self, string):
#         for i in range(len(string)):
#             self.insertSubstringStartingAt(i, string)
    
#     # Modified - no end symbol needed
#     def insertSubstringStartingAt(self, i, string):
#         node = self.root
#         for j in range(i, len(string)):
#             letter = string[j]
#             if letter not in node:
#                 node[letter] = {}
#             node = node[letter]
    
#     # Modified - do not need to finish at end symbol
#     def contains(self, string):
#         node = self.root
#         for i in range(len(string)):
#             letter = string[i]
#             if letter not in node:
#                 return False
#             node = node[letter]
#         return True


# Brute Force Solution
# Complexity O(bns) time | O(n) space
# where b is big string length, n is number of small strings,
# s is the length of the longest small string
# def multiStringSearch(bigString, smallStrings):
#     return [isInBigString(bigString, smallString) for smallString in smallStrings]


# def isInBigString(bigString, smallString):
#     for i in range(len(bigString)):
#         if i + len(smallString) > len(bigString):
#             break
#         if isInBigStringHelper(bigString, smallString, i):
#             return True
#     return False


# def isInBigStringHelper(bigString, smallString, startIdx):
#     leftBigIdx = startIdx
#     rightBigIdx = startIdx + len(smallString) - 1
#     leftSmallIdx = 0
#     rightSmallIdx = len(smallString) - 1
#     while leftBigIdx <= rightBigIdx:
#         if (
#             bigString[leftBigIdx] != smallString[leftSmallIdx] or
#             bigString[rightBigIdx] != smallString[rightSmallIdx]
#         ):
#             return False
#         leftBigIdx += 1
#         rightBigIdx -= 1
#         leftSmallIdx += 1
#         rightSmallIdx -= 1
#     return True
