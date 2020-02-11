# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        stack = [root]
        maxSum = [-float('inf'),0]
        lvl = 0
        while stack:
            currSum = 0
            nxtStack = []
            lvl += 1
            for node in stack:
                if node:
                    currSum += node.val
                    nxtStack.extend([node.left,node.right])
            stack = nxtStack
            
            if currSum > maxSum[0]:
                maxSum = [currSum,lvl]
            
        return maxSum[1]
            

        
        
        
            
        
        