# class Solution:
#     def maxProfit(self, prices):
#         if len(prices) == 0: return 0
#         tab = [0] * len(prices)
#         minPrice = prices[0]
#         for i,price in enumerate(prices):
#             if i > 0:
#                 if price - minPrice < tab[i-1]:
                    
#                     tab[i] = tab[i-1]
#                     if price - minPrice < 0: minPrice = price
#                 else:
#                     tab[i] = price - minPrice
            
#         return max(tab)


class Solution:
    def maxProfit(self, prices):
        maxCur,maxSoFar = 0,0
        for i in range(1,len(prices)): 
            maxCur += prices[i] - prices[i-1]
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)
            print(maxCur,maxSoFar,prices[i],prices[i-1])
        
        return maxSoFar

test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))