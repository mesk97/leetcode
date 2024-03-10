# https://leetcode.com/problems/minimum-window-substring/description/

# 76. Minimum Window Substring
# Hard
# Topics
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 1.2M
# Submissions
# 2.8M
# Acceptance Rate
# 41.7%
# Topics
# Hash Table
# String
# Sliding Window

# 23:11 fail

class Pattern:
    def __init__(self, s1):
        self.cleanup(s1)
        pass

    def cleanup(self, s1):
        self.container = dict()
        for s in s1:
            if s in self.container:
                self.container[s] = self.container[s] + 1
            else:
                self.container[s] = 1   

    def add(self, s):
        self.container[s] = self.container[s] - 1
        #print("add", s, self.container)
    
    def remove(self, s):
        self.container[s] = self.container[s] + 1
        #print("remove", s, self.container)

    def is_in_s1(self, s):
         return s in self.container
       
    def is_complete(self):
        # ТУДУ вот это еще за оптимайзить а то
        #  240 ms
        # Beats
        # 22.55%
        # of users with Python3
        for v in self.container.values():
            if v > 0:
                return False
        return True

    def find_next_in_pattern(self, cursor, s2):
        while cursor < len(s2) and not self.is_in_s1(s2[cursor]):
            cursor = cursor + 1
        return cursor


def main(s1, s2):
    result_len = 0
    result = ''

    pattern = Pattern(s1)
    
    begin = pattern.find_next_in_pattern(0, s2)
    end = pattern.find_next_in_pattern(0, s2)
    if end < len(s2):
        pattern.add(s2[end])

    #print (s1, s2)
    while end < len(s2):
        #print (begin, end, pattern.container)
        if pattern.is_complete():
            # 1. ТУДУ проверить и поменять минимум
            new_result_len = end - begin
            if result_len == 0 or new_result_len < result_len:
                result_len = new_result_len
                result = s2[begin:end+1]
        
            # 2. сдвинуть begin
            pattern.remove(s2[begin])
            begin = pattern.find_next_in_pattern(begin + 1, s2)
            continue

        end = pattern.find_next_in_pattern(end + 1, s2)
        if end < len(s2):
            pattern.add(s2[end])

    return result

if __name__ == "__main__":
    # s1 = "ab"
    # s2 = "eidbaooo"
    # s1 = "adc"
    # s2 = "dcda"

    s = "ADOBECODEBANC"
    t = "ABC"
    #s = "ab"
    #t = "b"
    print (main(t, s))
