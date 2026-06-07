# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node is None:
                return 0
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)
            self.ans = max(self.ans, l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        dfs(root)
        return self.ans