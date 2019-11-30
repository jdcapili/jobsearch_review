# import math
# class Solution:
#     def maxProfit(self, prices):
#         hold1,hold2 = -math.inf, -math.inf
#         release1,release2 = 0, 0
#         for i in prices:                           #   // Assume we only have 0 money at first
#             release2 = max(release2, hold2+i)      #// The maximum if we've just sold 2nd stock so far.
#             hold2    = max(hold2,    release1-i)   #// The maximum if we've just buy  2nd stock so far.
#             release1 = max(release1, hold1+i)      #// The maximum if we've just sold 1nd stock so far.
#             hold1    = max(hold1,    -i)           #// The maximum if we've just buy  1st stock so far. 
#             print("i is", i)
#             print(release2,hold2, release1,hold1)
#         return release2

    # def maxProfit(self, prices):
    #     if not prices:
    #         return 0
        
    #     # forward traversal, profits record the max profit 
    #     # by the ith day, this is the first transaction
    #     profits = []
    #     max_profit = 0
    #     current_min = prices[0]
    #     for price in prices:
    #         current_min = min(current_min, price)
    #         max_profit = max(max_profit, price - current_min)
    #         profits.append(max_profit)
    #     print(max_profit,profits)
    #     # backward traversal, max_profit records the max profit
    #     # after the ith day, this is the second transaction 
    #     total_max = 0    
    #     max_profit = 0
    #     current_max = prices[-1]
    #     for i in range(len(prices) - 1, -1, -1):

    #         current_max = max(current_max, prices[i])
    #         max_profit = max(max_profit, current_max - prices[i])
    #         total_max = max(total_max, max_profit + profits[i])
            
            
    #     return total_max

class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        
        profits = [0] * len(prices)
        c_m = prices[0]
        
        for i,price in enumerate(prices):
            if i > 0:
                c_m = min(c_m, price)
                profits[i] = max(profits[i-1],price-c_m)
                
            
        c_m, t_m, m_p = prices[-1],0,0
        
        for i,price in enumerate(reversed(prices)):
            
            c_m = max(c_m, price)
            m_p = max(m_p, c_m - price)
            t_m = max(t_m, m_p + profits[~i])

        return t_m
test = Solution()
print(test.maxProfit([3,3,5,0,0,3,1,4]))