'''
Given a string representation of the first n digits of Pi, and a list of positive integers
(all in string format), write a function that returns the smallest number of spaces
that can be added to the n digits of Pi such that all resulting numbers are found
in the list of integers.  A single number can appear multiple times in the resulting
numbers.  If no number of spaces to be added exists, such that all resulting numbers are
found in the list of integers, the function should return -1.
'''


# Complexity O(N^3 + M) time | O(N + M) where N is length of Pi argument,
# and M is the count of numbers substrings that we iterate through
def numbersInPi(pi, numbers):
	numbersTable = {number: True for number in numbers}
	minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
	return -1 if minSpaces == float("inf") else minSpaces
	
def getMinSpaces(pi, numbersTable, cache, idx):
	if idx == len(pi):
		return -1
	if idx in cache:
		return cache[idx]
	minSpaces = float("inf")
	for i in range(idx, len(pi)):
		prefix = pi[idx:i + 1]
		if prefix in numbersTable:
			minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
			minSpaces = min(minSpaces, minSpacesInSuffix + 1)
	cache[idx] = minSpaces
	return cache[idx]