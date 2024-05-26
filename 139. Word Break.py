# https://leetcode.com/problems/word-break/description/

# попытка 1 все ок но медленно
# Runtime
# 40
# ms
# Beats
# 57.66%
# of users with Python3
# Memory
# 16.56
# MB
# Beats
# 93.86%
# of users with Python3

# попытка 2 - выиграл время проиграл память
# Runtime
# 33
# ms
# Beats
# 90.49%
# of users with Python3
# Memory
# 16.76
# MB
# Beats
# 29.05%
# of users with Python3

# 139. Word Break
# Medium
# Topics
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.7M
# Submissions
# 3.6M
# Acceptance Rate
# 46.8%
# Topics
# Array
# Hash Table
# String
# Dynamic Programming
# Trie
# Memoization

def initiate(s, wordDict):
    cache = dict()

    for w in wordDict:
        #indices = []
        start = 0
        while True:
            index = s.find(w, start)
            if index == -1:
                break
            #indices.append(index)
            if not (index in cache):
                cache[index] = set()
            cache[index].add(len(w))
            start = index + 1
    
    return cache


def findWord(s, wordDict):
    lens = []

    for w in wordDict:
        index = str(s).find(w)
        if index == 0:
            lens.append(len(w))

    return lens 

def findWordWithCache(index):
    global cache
    if index in cache:
        return cache[index]
    return []

def main(s, wordDict):
    global cache
    cache = initiate(s, wordDict)

    results = [ False ] * (len(s) + 1)
    results[0] = True

    for i in range(0, len(s)):
        if not results[i]:
            continue

        #lens = findWord(s[i:], wordDict)
        lens = findWordWithCache(i)
        
        for l in lens:
            results[i + l] = True

    return results[len(s)]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]

    print(main(s, wordDict))