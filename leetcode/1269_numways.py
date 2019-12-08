# leetcode 1269
# example:
# steps = 3, arr = 2
# start with i = 0

class Solution:
    def numWays(self, steps: int, arrLen: int,pos=0, memo=None) -> int:
        if memo is None: memo = {}
        key = (steps,pos)
        if key in memo: 
            return memo[key]
        if pos < 0 or pos >= arrLen or steps < 0: return 0
        if pos == 0 and steps == 0: return 1
        
        
        c = 0
        c += self.numWays(steps-1,arrLen,pos-1,memo)        
        c += self.numWays(steps-1,arrLen,pos,memo)
        c += self.numWays(steps-1,arrLen,pos+1,memo)
        

        memo[key] = c % (10**9 + 7)
        return memo[key]
        
        