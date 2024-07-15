# https://leetcode.com/problems/edit-distance/description/

# 72. Edit Distance
# Medium
# Topics
# Companies
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 903.2K
# Submissions
# 1.6M
# Acceptance Rate
# 56.9%
# Topics
# String
# Dynamic Programming

# алго 
# используем D[x,y]
# где D это дистанция между словами 0,х и 0,y
# D[0, 1..x] = 1..x, D[1..y,0] = 1..y
# дальше в ручную заполняеем таблицу и смотрим  логику .. например rose и horse 
# E 4  4  3  3  3  2
# S 3  3  2  2  2  3
# O 2  2  1  2  3  4
# R 1  1  2  2  3  4
# # 0  1  2  3  4  5
#   #  H  O  R  S  E

# берем минимум из следующих вариантов
# 1. D[i, j-1]
# 2. D[i-1, j]
# 3. D[i-1, j-1]
# если a[i] != b[j] добавляем +1 

# fail1
# word1 =
# "intention"
# word2 =
# "execution"
# Output
# 4
# Expected
# 5

# fail2
# Wrong Answer
# 1127 / 1146 testcases passed
# Editorial
# Input
# word1 = 
# "zoologicoarchaeologist"
# word2 =
# "zoogeologist"
# Use Testcase
# Output
# 9
# Expected
# 10

# zoologicoarchaeologist
# zoo**g********eologist


def main(a, b):
    len_a = len(a)
    len_b = len(b)

    d = [[0] * (len_b + 1) for i in range(len_a + 1)]

    # D[0, 1..x] = 1..x, D[1..y,0] = 1..y
    for i in range(0, len_a + 1):
        d[i][0] = i
    for j in range(0, len_b + 1):
        d[0][j] = j
    
    for i in range(1, len_a + 1):
        for j in range (1, len_b + 1):
            if a[i-1] == b[j-1]:
                result = d[i-1][j-1]
            else:
                result = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
            
            # Вариант 2 с хаком
            #
            # if a[i-1] != b[j-1]:
            #     result = result + 1

            # # хак чтобы покрыть случай одинаковой буквы 
            # # без хака вот так 
            # #          o
            # #      [0, 1], 
            # #   o  [1, 0], 
            # #   l  [2, 1], 
            # #   o  [3, 1]
            # maximum = max(d[i][j-1], d[i-1][j], d[i-1][j-1])
            # if (maximum - result) > 1:
            #     result = result + 1 

            d[i][j] = result

    return d[len_a][len_b]

if __name__ == "__main__":
    word1 = "horse"
    word2 = "hormsesfdfdsfdsfdsfdsf"

    word1 = "intention"
    word2 = "execution"

    word1 = "zoologicoarchaeologist"
    word2 = "zoogeologist"

    #word1 = "zoologicoarcha"
    # word1 = "olo"
    # word2 = "o"


    #          o
    #      [0, 1], 
    #   o  [1, 0], 
    #   l  [2, 1], 
    #   o  [3, 1]


    # [
    #           e  x  e  c  u  t  i  o  n          
    #       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    #     i [1, 1, 2, 3, 4, 5, 6, 6, 7, 8],
    #     n [2, 2, 2, 3, 4, 5, 6, 7, 8, 8],
    #     t [3, 3, 3, 3, 4, 5, 5, 6, 7, 8], 
    #     e [4, 3, 4, 3, 3, 4, 5, 6, 7, 8], 
    #     n [5, 4, 5, 4, 4, 4, 5, 6, 7, 7], 
    #     t [6, 5, 6, 5, 5, 5, 4, 5, 6, 7], 
    #     i [7, 6, 7, 6, 6, 6, 5, 4, 5, 6], 
    #     o [8, 7, 8, 7, 7, 7, 6, 5, 4, 5], 
    #     n [9, 8, 9, 8, 8, 8, 7, 6, 5, 4]
    # ]

    print(main(word1, word2))
