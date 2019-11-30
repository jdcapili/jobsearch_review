class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        tab = [0] * len(prices)
        minPrice = prices[0]
        for i,price in enumerate(prices):
            if i > 0:
                if price - minPrice < tab[i-1]:
                    
                    tab[i] = tab[i-1]
                    if price - minPrice < 0: minPrice = price
                else:
                    tab[i] = price - minPrice
            
        return max(tab)


test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))