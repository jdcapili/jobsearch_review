# // Work through this problem on https://leetcode.com/problems/coin-change-2/ and use the specs given there.
# // Feel free to use this file for scratch work.
import collections
class Solution:
    def change(self, amount, coins, memo = None):
        if memo is None: memo = collections.defaultdict(int)
        memo[0] = 1
        for coin in coins:
            for i in range(coin, amount +1):
                print(i,coin)
                if i >= coin:
                    memo[i] += memo[i-coin]
        print(memo)            
        return memo[amount]
test = Solution()
test.change(5, [1,2,5])