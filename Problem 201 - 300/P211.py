class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = TrieNode()
                node = node.children[w]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        stack = [(node, word)]
        # dfs
        while stack:
            n, w = stack.pop()
            if not w:
                if n.isEnd:
                    return True
            elif w[0] == ".":
                for x in n.children.values():
                    stack.append((x, w[1:]))
            else:
                if w[0] in n.children:
                    stack.append((n.children[w[0]], w[1:]))
        return False
