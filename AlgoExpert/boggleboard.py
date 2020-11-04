'''
This function takes in a boggle board and checks a list of words to see
if they are contained in the boggle board (in a valid boggle pattern).  
If the words, are valid, then they will be returned from the function as part
of a new array of found words.

Inputs are two-dimensional rectangular array (a matrix) of potentially unequal
height and width: this matrix represents a boggle board as well as a list of
words to search for.

Valid boggle patterns are letters connected adjacent to one-another (horizontally,
vertically, diagonally) without any letter positions repeated to make one of the
words.  Valid words can overlap one another and letter positions can be used for
multiple words.
'''

# Complexity O(ws + nm * 8^s) time | O(ws + nm) space
# where w is number of words to check, s is the length of the longest word
# where n and m are the rows and columns of the boggle board matrix
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False


def getNeighbors(i, j, board):
    neighbors = []
    # top-left
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    # top
    if i > 0:
        neighbors.append([i - 1, j])
    # top-right
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    # right
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    # bottom-right
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    # bottom
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    # bottom-left
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    # left
    if j > 0:
        neighbors.append([i, j - 1])
    return neighbors


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
