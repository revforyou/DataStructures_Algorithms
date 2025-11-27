class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
    
    def _dfs(self, word, i, node):
        # if we reached end of search word
        if i == len(word):
            return node.end
        
        c = word[i]
        
        # Case 1: normal letter
        if c != '.':
            if c not in node.children:
                return False
            return self._dfs(word, i + 1, node.children[c])

        # Case 2: c == '.', try all possible children
        for child in node.children.values():
            if self._dfs(word, i + 1, child):
                return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)