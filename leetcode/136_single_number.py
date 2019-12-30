class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.defaultdict(int)
        for num in nums:
            c[num] += 1
        
        for k,v in c.items():
            if v == 1: return k