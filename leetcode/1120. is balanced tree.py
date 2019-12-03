# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        BalancedStatsWHeight = collections.namedtuple('BalancedStatsWHeight',('balanced','height'))
        
        def check_balanced(tree):
            if not tree:
                return BalancedStatsWHeight(True,-1)
            
            left_res = check_balanced(tree.left)
            if not left_res.balanced:
                return BalancedStatsWHeight(False,0)
            
            right_res = check_balanced(tree.right)
            if not right_res.balanced:
                return BalancedStatsWHeight(False,0)
            
            is_balanced = abs(left_res.height - right_res.height) <= 1 # at most 1
            height = max(left_res.height, right_res.height) + 1
            return BalancedStatsWHeight(is_balanced, height)
    
        
        return check_balanced(root).balanced