class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pd = 1 
        sd = 0
        while n > 0:
            digit = n % 10
            pd *= digit
            sd += digit
            n = n // 10
        
        return pd - sd