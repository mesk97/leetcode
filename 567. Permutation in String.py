# # Hash Table
# Two Pointers
# String
# Sliding Window
# https://leetcode.com/problems/permutation-in-string/description/

# 567. Permutation in String
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 792.6K
# Submissions
# 1.8M
# Acceptance Rate
# 44.3%
# Topics
# Hash Table
# Two Pointers
# String
# Sliding Window

# 21:44
# 22:20 - first try 98/108
# 22:26

class Pattern:
    def __init__(self, s1):
        self.cleanup(s1)
        pass

    def cleanup(self, s1):
        self.container = dict()
        self.symbols = len(s1)
        for s in s1:
            if s in self.container:
                self.container[s] = self.container[s] + 1
            else:
                self.container[s] = 1   

    def add(self, s):
        self.container[s] = self.container[s] - 1
        self.symbols = self.symbols - 1
    
    def remove(self, s):
        self.container[s] = self.container[s] + 1
        self.symbols = self.symbols + 1

    def is_in_s1(self, s):
        return s in self.container
    
    def is_over(self, s):
        return (self.container[s] - 1) < 0
    
    def is_complete(self):
        return self.symbols == 0

def main(s1, s2):
    begin = 0
    end = 0

    pattern = Pattern(s1)
    #print(s1, s2)

    while end < len(s2):
        #print(begin, end, s2[begin], s2[end], pattern.container)

        if pattern.is_complete():
            return True

        if not pattern.is_in_s1(s2[end]):
            pattern.cleanup(s1)
            end = end + 1
            begin = end
            continue
        
        if pattern.is_over(s2[end]):
            pattern.remove(s2[begin])
            begin = begin + 1
            continue

        pattern.add(s2[end])
        end = end + 1

    return pattern.is_complete()

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    s1 = "adc"
    s2 = "dcda"
    print (main(s1, s2))
