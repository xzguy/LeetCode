class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: [str]):
        self.queries = []
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        i = len(self.queries) - 1
        node = self.trie.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.queries[i] not in node.children:
                return False
            node = node.children[self.queries[i]]
            i -= 1
        return node.isEnd

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)