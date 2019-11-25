class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for idx, ele in enumerate(nums):
            start = idx + 1
            end = len(nums) - 1
            while start < end:
                sums = ele + nums[start] + nums[end]
                if sums == 0:
                    ans.add((ele, nums[start], nums[end]))
                    
                if sums <= 0: start += 1
                else: end -= 1
                    
        return ans