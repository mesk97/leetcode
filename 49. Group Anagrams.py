# Arrays & Hashing

# https://leetcode.com/problems/group-anagrams/description/
# 49. Group Anagrams
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


def main(strs):
    anagram_set = dict()

    for s in strs:
        normalized = ''.join(sorted(s))
        if normalized in anagram_set:
            anagram_set[normalized].append(s)
        else:
            anagram_set[normalized] = [s]

    out = []
    for i in anagram_set.values():
        out.append(i)
    return out


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(main(strs))