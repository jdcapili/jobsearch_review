class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        mid = (len(nums) // 2)
        l, r = nums[0:mid-1], nums[mid:len(nums)]
        ref = TreeNode(nums[mid])
        [-3,-5]
        treenode(-3)
            [-11,-10]
        

test = Solution()
test.sortedArrayToBST([-11,-10,-3,0,5,9,10])