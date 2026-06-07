# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(root):
            if root is None:
                return 0
            ldepth = depth(root.left)
            rdepth = depth(root.right)
            self.ans = max(self.ans, ldepth + rdepth)
            return 1 + max(ldepth, rdepth)
        depth(root)
        return self.ans