# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            l = len(queue)
            res.append(queue[-1].val)
            for _ in range(l):
                el = queue.popleft()
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
        return res
        