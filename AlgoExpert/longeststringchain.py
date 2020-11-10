'''
Function that given a list of strings, returns the longest string chain that can
be built from those strings.

A string chain is defined as a string "A" in the initial array - if removing any
single character from string "A" yields a new string "B" that is in the initial
array of strings, then "A" and "B" form a string chain. Similarly, if removing
any single character in string "B", yields string "C" contained in the list
of strings, it can also be part of the string chain.

Only one longest string chain can be possible in the input.
'''
# Complexity O(n * m^2 + n log(n)) time | O(nm) space
# Where n is the number of strings in the list input
# and m is the number of characters in the longest of the strings
# Time complexity can be improved by n log(n) if we drop the strings sorting step
# but this will require much more complexity, adding checks to see
# if the shorter strings than the current iteration element have had their hash tables built
def longestStringChain(strings):
    stringChains = {}
    for string in strings:
        stringChains[string] = {"nextString": "", "maxChainLength": 1}
    sortedStrings = sorted(strings, key=len)
    for string in sortedStrings:
        findLongestStringChain(string, stringChains)
    
    return buildLongestStringChain(strings, stringChains)
        

def findLongestStringChain(string, stringChains):
    for i in range(len(string)):
        smallerString = getSmallerString(string, i)
        if smallerString not in stringChains:
            continue
        tryUpdateLongestStringChainLength(string, smallerString, stringChains)

def getSmallerString(string, index):
    return string[0:index] + string[index + 1 :]

def tryUpdateLongestStringChainLength(currentString, smallerString, stringChains):
    smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
    currentStringChainLength = stringChains[currentString]["maxChainLength"]
    if smallerStringChainLength + 1 > currentStringChainLength:
        stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
        stringChains[currentString]["nextString"] = smallerString

def buildLongestStringChain(strings, stringChains):
    maxChainLength = 0
    chainStartingString = ""
    for string in strings:
        if stringChains[string]["maxChainLength"] > maxChainLength:
            maxChainLength = stringChains[string]["maxChainLength"]
            chainStartingString = string

    ourLongestStringChain = []
    currentString = chainStartingString
    while currentString != "":
        ourLongestStringChain.append(currentString)
        currentString = stringChains[currentString]["nextString"]

    return [] if len(ourLongestStringChain) == 1 else ourLongestStringChain
