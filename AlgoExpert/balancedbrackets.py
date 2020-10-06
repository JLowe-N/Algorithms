"""
Given a string of characters, check to see if square, round, and curly brackets 
are balanced.  Function will return a boolean testing if brackets are balanced.
"""

# Complexity - Time O(N) | Space O(N) where N is the length of the given string
def balancedBrackets(string):
    openingBrackets = '([{'
    closingBrackets = ')]}'
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
