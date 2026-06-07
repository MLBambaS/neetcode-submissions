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
        i = 0
        for c in word:
            i+=1
            if c != '.':
                if c not in node.children:
                    return False
                node = node.children[c]
            else:
                if not node.children: return False
                check = False
                for key in node.children.keys():
                    if i == len(word):
                        check = node.children[key].isWord
                    else: check = self.searchEnd(node.children[key], word[i:])
                    if check: return True
                return False
        return node.isWord    
        
class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False