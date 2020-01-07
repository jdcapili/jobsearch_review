class Solution:
    def coinChange(self, coins: List[int], amount: int,memo = None) -> int:
        
        
        tab = [0] + [float('inf')] * amount
        
        for coin in coins:
            for x in range(coin,amount+1):
                tab[x] = min(tab[x],tab[x-coin] + 1)
        return tab[amount] if tab[amount] != float('inf') else -1