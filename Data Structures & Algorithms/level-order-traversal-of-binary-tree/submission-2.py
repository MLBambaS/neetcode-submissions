# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            l = len(queue)
            level = []
            for _ in range(l):
                el = queue.popleft()
                level.append(el.val)
                if el.left: 
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            res.append(level)
        return res