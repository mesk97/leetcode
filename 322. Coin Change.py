# https://leetcode.com/problems/coin-change/description/


# Time Limit Exceeded
# 15 / 189 testcases passed
# coins = [1,2,5]
# amount = 100

# 322. Coin Change
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.8M
# Submissions
# 4.1M
# Acceptance Rate
# 44.0%
# Topics
# Array
# Dynamic Programming
# Breadth-First Search

def mainRecursive(coins, amount):
    if amount == 0:
        return 0
    
    global cache
    if amount in cache:
        return cache[amount]

    result = -1
    for c in coins:
        if (amount - c) < 0:
            continue

        prev = mainRecursive(coins, amount - c)
        if prev < 0:
            continue
        if result < 0:
            result = prev
            continue
        result = min(result, prev)
    
    if result < 0:
        return result
    return result + 1

def mainDirect(coins, amount):
    result = -1
    results = [ -1 ] * (amount + 1)
    results[0] = 0

    for i in range(0, amount):
        if results[i] < 0:
            continue
        for c in coins:
            if (i + c) > amount:
                continue
            newresult = results[i] + 1
            if results[i + c] < 0:
                results[i + c] = newresult
                continue

            results[i + c] = min(newresult, results[i + c])

    return results[amount]

def main(coins, amount):
    global cache
    cache = set()
    return mainDirect(coins, amount)

if __name__ == "__main__":


    coins = [1,2,5]
    amount = 11

    coins = [2]
    amount = 3

    coins = [1,2,5]
    amount = 100

    print(main(coins, amount))
