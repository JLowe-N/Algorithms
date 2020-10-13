'''
Given a list of items represented by a subarray where index 0 is the value of the item
and index 1 is the weight of the item.  Given a sack with a specified weight capacity (integer),
optimize for the highest value given the weight capacity, noting that only a single (whole) item
can be selected - no fractions or multiples of any item.
'''

# Implementation - Dynamic Programming - Capacity in columns, items in rows
# Complexity - Time O(Nc) | Space O(Nc) - N # of items, c - capacity specified


def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(capacity + 1)]
                      for y in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(
                    knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]


def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1
    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
