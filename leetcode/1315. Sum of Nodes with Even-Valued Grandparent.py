class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getSum(parent,node,res = 0):
            if not node: return res
            if parent is not None and parent % 2 == 0:
                if node.left: 
                    res += node.left.val
                if node.right: 
                    res += node.right.val
            res = getSum(node.val,node.left,res)
            res = getSum(node.val,node.right,res)
            return res
        
        return getSum(None, root)