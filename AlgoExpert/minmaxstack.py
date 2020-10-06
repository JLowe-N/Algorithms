"""
Stack implementation that keeps track of the min and max of the stack at 
all positions.

Operations Time Complexity is O(1) for each single use of its methods while
overall Space Complexity is O(N) where N is the total number of elements that will
be added to the stack.  There will be N storage on the stack itself, as well as
N storage on the minMaxStack.  This simplifies to O(N) storage complexity overall
 
"""
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]
