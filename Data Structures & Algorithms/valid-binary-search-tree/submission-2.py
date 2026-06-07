# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            l = dfs(node.left, low, node.val)
            r = dfs(node.right, node.val, high)
            return l and r
        return dfs(root, float("-inf"), float("inf"))