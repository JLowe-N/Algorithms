'''
Given three inputs of class AncestralTree with properties ancestor and name,
find the youngest common ancestor and return the the AncestralTree node of that
ancestor.
'''


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Complexity O(d) Time - where d is the depth of the deepest descendant
# O(1) Space - Constant Space Complexity


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        diff -= 1
        lowerDescendant = lowerDescendant.ancestor
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant
