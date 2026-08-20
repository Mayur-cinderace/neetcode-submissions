class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEnd = True    

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                return False
            node = node.children[i]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if node.children[i] is None:
                return False
            node = node.children[i]
        return True
