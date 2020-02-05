# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def convert(root):
            if root is None: return 0
            
            convert(root.right)
            root.val += self.sum
            self.sum = root.val
            convert(root.left)
            
        convert(root)
        return root