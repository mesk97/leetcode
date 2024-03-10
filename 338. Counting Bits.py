# https://leetcode.com/problems/counting-bits/
# 338. Counting Bits
# Easy
# 10.6K
# 481
# Companies
# Given an integer n, return an array ans of length n + 1 such that for each i(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Example 1:

# Input: n = 2
# Output: [0, 1, 1]
# Explanation:
# 0 - -> 0
# 1 - -> 1
# 2 - -> 10
# Example 2:

# Input: n = 5
# Output: [0, 1, 1, 2, 1, 2]
# Explanation:
# 0 - -> 0
# 1 - -> 1
# 2 - -> 10
# 3 - -> 11
# 4 - -> 100
# 5 - -> 101


# Constraints:

# 0 <= n <= 105


# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass ?
# Can you do it without using any built-in function(i.e., like __builtin_popcount in C++)?

# Algo:
# X1 = 1
#   имеем каунтер докуда дошли CALCULATED
#   и идем от J = 1 до CALCULATED
#   x[J+CALCULATED] = X[J] + 1

def main(n):
    mas = (n+1) * [0]

    calculated = 1
    mas[0] = 0

    while True: 
        for i in range(0, calculated):
            if (i + calculated) > n:
                return mas[0:]
            mas[i + calculated] = 1 + mas[i]
        calculated = 2 * calculated

    return None

if __name__ == "__main__":
    n = 8
    print(main(n))
