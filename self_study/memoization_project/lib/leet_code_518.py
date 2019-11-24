// Work through this problem on https://leetcode.com/problems/coin-change-2/ and use the specs given there.
// Feel free to use this file for scratch work.

class Solution:
    def change(self, amount: int, coins: List[int], memo = None) -> int:
        if memo is None: memo = {}

        if amount == 0: return 1
        if amount in memo: return memo[amount]

        num_coins = []
        for coin in coins:

            if coin <= amount:
                print(coin, amount - coin)
        num_coins.append(self.change(amount - coin, coins, memo) + 1)

        memo[amount] = len(num_coins)
        print(memo)
return memo[amount]