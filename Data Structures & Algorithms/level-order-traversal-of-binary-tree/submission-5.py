# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque([root])
        results = []
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):

                node = q.popleft()
                if node is None:
                    return results
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                level.append(node.val)
            results.append(level)
        return results