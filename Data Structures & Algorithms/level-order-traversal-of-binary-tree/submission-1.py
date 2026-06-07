# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res=[]
        level=1
        while queue:
            nextLevel=0
            l=[]
            for i in range(level):
                node = queue.popleft()
                if not node:
                    continue
                else:
                    l.append(node.val)
                    if node.left:
                        nextLevel+=1
                        queue.append(node.left)
                    if node.right:
                        nextLevel+=1
                        queue.append(node.right)
            level=nextLevel
            if l: res.append(l)
        return res
                    
