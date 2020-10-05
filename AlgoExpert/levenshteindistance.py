# Given 2 strings, find the minimum number of edits
# (insertions, deletions, or substitutions) to make str1 equal str2

# Find shorter of 2 strings, this will be columns
# This will provide an additional optimization to Space complexity
# Smaller string should be in columns of dynamic array
# Complexity Time O(n x m) | Space O(min(n, m))
def levenshteinDistance(str1, str2):
    # small is column direction, big is row direction
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]


# Complexity Time O(n x m) | Space O(n x m) - only need last 2 rows though!
# Can be improved
# def levenshteinDistance(str1, str2):
#     # Initialize a 2D array of that will compare str1 to str2 and find the
#     # minimum # of edits to transform each substring
#     edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     # Reset 1st column to reference range(len(index) + 1) for str2
#     for i in range(1, len(str2) + 1):
#         edits[i][0] = i
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             # if character at index i - 1, j - 1 the same, no additional changes needed for current iteration
#             if str2[i - 1] == str1[j - 1]:
#                 edits[i][j] = edits[i - 1][j - 1]
#             # otherwise, 1 additional change needed, find path with minimum # of changes
#             else:
#                 edits[i][j] = 1 + min(edits[i - 1][j - 1],
#                                       edits[i][j - 1], edits[i - 1][j])
#     return edits[-1][-1]
