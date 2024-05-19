# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# 746. Min Cost Climbing Stairs
# Easy
# Topics
# Companies
# Hint
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 1.8M
# Acceptance Rate
# 65.7%
# Topics
# Array
# Dynamic Programming

# dp[1] = cost
# dp[n] = min(dp[n-1] + cost[n-1], dp[n-2] + cost[n-2])

def find_min(dp, cost, i, increment, size):
    if (i + increment) > size:
        return 
    if dp[i + increment] is None:
        dp[i + increment] = dp[i] + cost[i]
        return
    dp[i + increment] = min(dp[i + increment], dp[i] + cost[i])


def main(cost):
    size = len(cost)
    dp = [None] * (size + 1)
    result = 0

    dp[0] = 0
    dp[1] = 0

    for i in range(0, size):
        find_min(dp, cost, i, 1, size)
        find_min(dp, cost, i, 2, size)

    return dp[size]

if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    #cost = [10,15,20]

    print (main(cost))