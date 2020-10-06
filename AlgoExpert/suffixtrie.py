"""
Suffix trie maps all possible suffixes that can be found from a string, and 
allows searching for a suffix in the base string to happen in O(m) time where
m is the length of the search string

Faster suffix trie creation is possible, but the algorithm is more difficult
to implement and representation is also different.  This can be done in O(N) time
(See Ukkonen's algorithm for more details)
"""


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Complexity - Time O(N^2) time | O(N^2) space where N is length of trie base string
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    # Complexity - Time O(m) time | O(1) space where m is the length of search string
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
