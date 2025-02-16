from typing import List
"""
Input: [7,10] amount = 94
Output: 10 (2 * 7 + 8 * 10 = 94)

Input: coins = [1, 2, 5], amount = 11  
Output: 3

Dry run:
Input: coins = [1, 2], amount = 3 
Output: 

[] 3 (2)            
|
[1] 2 (2)
|              |
[1,1] 1 (3)  [1,2] 3 (2)
|            |
[1,1,1] 0  [1,1,2] -1


|
[2] 1  (2)
|                |
[2,1] 0 (2)    [2,2] -1

memo = {
    1: 1
    2: 1
}

42 mins to solve
"""
def coin_change(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1

    memo = {}  # { amount: min_coins }
    def dfs(coins_used, cur_amt):
        if cur_amt in memo:
            return coins_used + memo[cur_amt]

        if cur_amt == 0:
            return coins_used
        elif cur_amt < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, dfs(coins_used + 1, cur_amt - coin))

        memo[cur_amt] = min_coins - coins_used

        return min_coins

    result = dfs(0, amount)

    if result == float('inf'):
        return -1
    else:
        return result

# debug your code below
print(coin_change([1, 2, 5], 11))
# print(coin_change([1, 2], 3))
