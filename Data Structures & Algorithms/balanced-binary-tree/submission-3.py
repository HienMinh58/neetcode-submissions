# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            l_depth = dfs(node.left)
            if l_depth == -1:
                return -1
            r_depth = dfs(node.right)
            if r_depth == -1:
                return -1
            if abs(l_depth - r_depth) > 1:
                return -1
            return 1 + max(l_depth, r_depth)
        return dfs(root) != -1