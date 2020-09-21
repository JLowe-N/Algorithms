# Given an m x n array, return a flat array that traverses the original array
# in a clockwise spiral pattern

# O(N) Time Complexity
# O(N) Space Complexity

# Iterative Implementation
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        for col in reversed(range(startCol, endCol - 1 + 1)):
            # Edge case for single row in middle matrix
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            # Edge case for single column in middle matrix
            if startCol == endCol:
                break
            result.append(array[row][startCol])
        
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    
    return result

# O(N) Time Complexity
# O(N) Space Complexity - for result array storage, but also recursion call stack 

# Recursive Implementation
"""
def spiralTraverse(array):
	spiral = []
	endCol = len(array[0]) - 1
	endRow = len(array) - 1
	spiralHelper(array, spiral, endCol, endRow)
	return spiral

def spiralHelper(array, spiral, eC, eR, sC = 0, sR = 0):
    # Base / Edge Cases
	if sR > eR or sC > eC:
		return
	if sR == eR and sC == eC:
		spiral.append(array[sR][sC])
		return
	if sR == eR and sC < eC:
		for c in range(sC, eC + 1):
			spiral.append(array[sR][c])
		return
	if sC == eC and sR < eR:
		for r in range(sR, eR + 1):
			spiral.append(array[r][sC])
		return

    # Main Logic for traversing perimeter    
	for c in range(sC, eC + 1):
		spiral.append(array[sR][c])
	for r in range(sR + 1, eR + 1):
		spiral.append(array[r][eC])
	for c in reversed(range(sC, eC - 1 + 1)):
		spiral.append(array[eR][c])
	for r in reversed(range(sR + 1, eR - 1 + 1)):
		spiral.append(array[r][sC])
	spiralHelper(array, spiral, eC - 1, eR - 1, sC + 1, sR + 1)
"""
		
	
	
	
		


    