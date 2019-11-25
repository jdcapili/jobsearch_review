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


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            dp = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in dp:
                    temp = tuple(sorted([nums[i], target - nums[j], nums[j]]))
                    unique.add(temp)
                dp.add(nums[j])
        return unique