'''
Given a rectangular 2D array, traverse the array in a zigzag pattern, returning
a flattened array.  Zigzag order starts at the top left corner, goes down
by one, and proceeds in a zig zag pattern all the way to the bottom-right corner.
'''

# Complexity - O(N) Time | O(N) Space where N is the number of elements in the
# input array
def zigzagTraverse(array):
    result = []
    height = len(array) - 1
    width = len(array[0]) - 1
    row, col = 0, 0
    goingDown = True
    while not isOutOfBounds(array, height, width, row, col):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def isOutOfBounds(array, height, width, row, col):
    return row < 0 or row > height or col < 0 or col > width
