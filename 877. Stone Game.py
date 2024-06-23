# https://leetcode.com/problems/stone-game/description/

# 877. Stone Game
# Medium
# Topics
# Companies
# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

# Example 1:

# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
# Example 2:

# Input: piles = [3,7,2,3]
# Output: true
 

# Constraints:

# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 237.7K
# Submissions
# 336.4K
# Acceptance Rate
# 70.6%
# Topics
# Array
# Math
# Dynamic Programming
# Game Theory


# 1. проходим рекурсивно вниз
# 2. D_A[0, n-1] = Max_A( piles[0]+D_B[1, n-1], piles[n-1]+D_B[0,n-2])
#     Max_A -> оначает что максимизируем по Алисе, D_B означает что стартует первым Боб

# запуск без кэша
# Time Limit Exceeded
# 26 / 46 testcases passed

# финалочка
# Runtime
# 443
# ms
# Beats
# 14.72%
# Analyze Complexity
# Memory
# 48.89
# MB
# Beats
# 27.84%

def D(piles, start_index, end_index, is_A, result_A, result_B):
    global cache

    if (start_index, end_index, is_A) in cache:
        return cache[(start_index, end_index, is_A)]

    # краевой случай
    if (end_index - start_index) == 1:
        if is_A:
            result_A = result_A + piles[start_index]
        else:
            result_B = result_B + piles[start_index]
        
        cache[(start_index, end_index, is_A)] = (result_A, result_B)
        return (result_A, result_B)

    # случай 1: начало
    (result_A_1, result_B_1) = D(piles, start_index + 1, end_index, not is_A, result_A, result_B)
    if is_A:
        result_A_1 = result_A_1 + piles[start_index]
    else:
        result_B_1 = result_B_1 + piles[start_index]

    # случай 2: конец
    (result_A_2, result_B_2) = D(piles, start_index, end_index - 1, not is_A, result_A, result_B)
    if is_A:
        result_A_2 = result_A_2 + piles[end_index - 1]
    else:
        result_B_2 = result_B_2 + piles[end_index - 1]
    
    # сравниавем результат
    result_A = result_A_1
    result_B = result_B_1
    if is_A:
        if result_A_2 > result_A_1:
            result_A = result_A_2
            result_B = result_B_2
    else:
        if result_B_2 > result_B_1:
            result_A = result_A_2
            result_B = result_B_2

    cache[(start_index, end_index, is_A)] = (result_A, result_B)
    return (result_A, result_B)

def main(piles):
    global cache
    cache = dict()

    (result_A, result_B) = D(piles, 0, len(piles), True, 0, 0)
    #return (result_A, result_B)
    return result_A > result_B

if __name__ == "__main__":
    piles = [5,3,4,5]
    piles = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
    print(main(piles))