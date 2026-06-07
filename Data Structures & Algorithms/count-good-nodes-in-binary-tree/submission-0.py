# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        queue = deque([(root, root.val)])
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node, maxAnc = queue.popleft()
                if node.left:
                    if node.left.val >= maxAnc:
                        count+=1
                    queue.append((node.left, max(maxAnc, node.left.val)))
                if node.right:
                    if node.right.val >= maxAnc:
                        count+=1
                    queue.append((node.right, max(maxAnc, node.right.val)))
        return count

        