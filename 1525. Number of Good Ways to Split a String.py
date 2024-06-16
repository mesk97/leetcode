# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/

# 1525. Number of Good Ways to Split a String
# Medium
# Topics
# Companies
# Hint
# You are given a string s.

# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

# Return the number of good splits you can make in s.

 

# Example 1:

# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
# Example 2:

# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 102.3K
# Submissions
# 149.7K
# Acceptance Rate
# 68.3%
# Topics
# Hash Table
# String
# Dynamic Programming
# Bit Manipulation

# Runtime
# 164
# ms
# Beats
# 12.34%
# Analyze Complexity
# Memory
# 17.97
# MB
# Beats
# 25.80%

class Mapa:
    def __init__(self) -> None:
        self.internal = dict()
        self.result = 0
        pass

    def add(self, symbol):
        if not symbol in self.internal:
            self.internal[symbol] = 1
            self.result = self.result + 1
            return
        self.internal[symbol] = self.internal[symbol] + 1

    def delete(self, symbol):
        self.internal[symbol] = self.internal[symbol] - 1
        if self.internal[symbol] == 0:
            self.result = self.result - 1

    def getResult(self):
        return self.result

def main(s):
    result = 0

    # 1. создаем мапу - какая буква сколько раз встречалась
    right = Mapa()
    left = Mapa()

    # 2. первый раз проходим и заполняем мапу 
    for symbol in list(s):
        right.add(symbol)

    # 3. проходим второй раз 
    for symbol in list(s):
    #    3.1 заполняем мапу слева и убираем из мапы справа
        left.add(symbol)
        right.delete(symbol)
        if left.getResult() == right.getResult():
            result = result + 1
    # 4. если кол-во равно плюсуем резал
    return result

if __name__ == "__main__":
    s = "aacaba"
    print(main(s))