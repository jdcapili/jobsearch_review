class Node:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

# class Solution:
    # def minDepth(self, root, c=0):
    #     if not root: return c
        
    #     c += 1
    #     left = self.minDepth(root.left,c)
    #     right = self.minDepth(root.right,c)
        
    #     return min(left,right)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif not root.left and root.right:
            return 1+ self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

test = Node(3)
a = Node(9)
b = Node(20)
c = Node(15)
d = Node(17)

test.left = a
test.right = b
b.left = c
b.right = d

testcase = Solution()
print(testcase.minDepth(test))