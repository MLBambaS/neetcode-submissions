class TriNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def add(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TriNode()
            node = node.children[c]
        node.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TriNode()
        res=set()
        for word in words:
            trie.add(word)
        def backtracking(r, c, visited, trie, current):
            if r<0 or c<0 or r==len(board) or c==len(board[0]) or (r,c) in visited:
                return
            x = board[r][c]
            if x not in trie.children:
                return
            visited.add((r,c))
            if trie.children[x].isWord: 
                res.add(current+x)
            backtracking(r+1, c, visited, trie.children[x], current+x)
            backtracking(r-1, c, visited, trie.children[x], current+x)
            backtracking(r, c+1, visited, trie.children[x], current+x)
            backtracking(r, c-1, visited, trie.children[x], current+x)
            visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                backtracking(r, c, set(), trie, "")
        return list(res)


        