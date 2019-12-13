
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.right,root.left = root.left,root.right
        return root