class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        i = 0
        while i < len(nums):
            res += min(nums[i],nums[i+1])
            i += 2
        return res
            