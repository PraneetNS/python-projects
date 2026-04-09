

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        Left = self.maxDepth(root.left)
        Right = self.maxDepth(root.right)
        return 1+max(Left,Right)