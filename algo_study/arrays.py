# def buy_and_sel1_stock_twice (prices) :
#     max_total_profit, min_price_so_far = 0.0, float('inf')
#     first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maxinum profit if we sel_l on that
    # day.
    # for i, price in enumerate(prices):
    #     min_price_so_far = min(min_price_so_far, price)
    #     max_total_profit = max(max_total_profit, price - min_price_so_far)
    #     first_buy_sell_profits[i] = max_total_profit
    # Backward phase. For each day, find the naxinun profit if we nake the
    # second buy on that day.
    
    # max_price_so_far = float(' -inf ')
    
#     for i, price in reversed(list(enumerate(prices[1:], 1))):
#         max_price_so_far = max(max_price_so_far, price)
#         max_total_profit = max(
#             max_total_profit,
#             max_price_so_far - price + first_buy_sell_profits[i - 1])
        
#     return max_total_profit

# print(buy_and_sel1_stock_twice([12,11,13,9,12,8,14,13,15]))

# def rearrange(arr):
#     i = 1
#     while i < len(arr):
#         if i % 2 == 1 and arr[i-1] >= arr[i]:
#             arr[i - 1], arr[i] = arr[i], arr[i-1]
#         elif i % 2 == 0 and arr[i-1] <= arr[i]:
#             arr[i - 1], arr[i] = arr[i], arr[i-1]
#         i += 1
#     print(arr)

# rearrange([7,3,2,5,8,9])

# def generate-primes (n) :
#     if n < 2:
#         return []
#     size= (n-3) // 2 + 1
#     primes = [2] # Stores the prizes fron 7 to n.
# is-prineliJ represents (2i + 3) is prine or not.
# InitialTy set each to true. Then use sieving to elininate nonprines.
    # is_prime=[True] * size
    # for i in range(size):
    #     if is_prime[i]:
    #         p=i*2+3
    #     primes.append(p)
# Sieving fron p^2, where p^2 = (4i^2 + 12i + 9). The index in is-prirne
# is (2i^2 + 6i + 3) because is*prinefi] represents 2i + 3.
#
# Note that we need to use Tong for j because p^2 night overfTow.
    #     for j in range(2 * i**2 + 6 * i + 3, size, p):
    #         is_prime[j] = False
    # return primes

import random
def sample_offline_data(arr,size):
    for i in range(0,size):
        r = random.randint(i, len(arr)-1)
        arr[r],arr[i] = arr[i], arr[r]
    
    print(arr)

sample_offline_data([3,4,6,7,8,9],2)