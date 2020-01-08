class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        chars = [str(num) for num in nums]
        c = 0
        for char in chars:
            if len(char) % 2 == 0: c += 1
        
        return c