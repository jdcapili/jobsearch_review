class Solution(object):
    def twoSum(self, nums, target):
        dicti = {}
        
        for i in range(len(nums)):
            if nums[i] in dicti:
                return [dicti[nums[i]], i]
            else:
                diff = target - nums[i]
                dicti[diff] = i
        
        