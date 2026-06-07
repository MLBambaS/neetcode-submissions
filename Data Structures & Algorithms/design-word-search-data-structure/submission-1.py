class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.searchEnd(self.root, word)

    def searchEnd(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c != '.':
                if c not in node.children:
                    return False
                node = node.children[c]
            else:
                # Pour un joker, essayer tous les enfants possibles
                for child in node.children.values():
                    if self.searchEnd(child, word[i+1:]):
                        return True
                return False
        return node.isWord   
        
class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False