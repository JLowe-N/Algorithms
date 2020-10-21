'''
Given a pattern consisting of x and/or y characters that represent a substring of a given string,
find a return an array of x and y substrings that will fill the pattern to match the given string.

There will only be 1 correct pair (if any) of x and y substrings that will match the given
string when the pattern is applied.  Both inputs will be non-empty strings.

If no possible matching pattern, return an empty array.
'''

# Complexity - O(n^2 + m) time | O(n + m) space
# Where n is the length of the main string and m is the length of the pattern
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)
    if counts["y"] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            x = string[:lenOfX]
            y = string[yIdx:yIdx + lenOfY]
            potentialMatch = map(lambda char: x if char =="x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        lenOfX = len(string) / counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]
    return []

def getNewPattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char =="y" else "y", patternLetters))

def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos