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
            if not root:
                return 0
            ld = depth(root.left)
            rd = depth(root.right)
            self.ans = max(self.ans, ld + rd)

            return 1 + max(ld, rd)
        depth(root)
        return self.ans