# 438. Find All Anagrams in a String
# Medium
# 9.3K
# 287
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=algorithm-ii

def main2(s, p):
    found_patterns = []
    matched_str = []
    processed = 0

    found = dict()
    for i in str(p):
        found[i] = None

    for element in str(s):
        print (element, found, matched_str)
        if element in p:
            if found[element] == None:
                found[element] = processed
            else:
                print ("here1", processed, found[element])
                if (processed - found[element]) <= len(p):
                    print ("here2")

                    to_delete = len(p) - (processed - found[element]) + 1
                    print ("here3", to_delete, processed, found[element])
                    for i in range(0, to_delete):
                        print ("here4", matched_str[0])
                        found[matched_str[0]] = None
                        del matched_str[0]
                    found[element] = processed

            matched_str.append(element)
            if (len(matched_str) == len(p)):
                print ("!!!!")
                found_patterns.append(processed - len(p) + 1)

        else:
            matched_str = []
            found = dict()
            for i in str(p):
                found[i] = None

        processed = processed + 1

    return found_patterns

def all_is_zero(hashes):
    for v in dict(hashes).values():
        if v != 0:
            return False
    return True

def main(string, pattern):
    begin_window = 0
    end_window = -len(pattern)
    letters = list(string)
    found_patterns = []
    hashes = dict()

    for i in string:
        hashes[i] = 0
    for i in pattern:
        if not (i in hashes):
            hashes[i] = 0 
        hashes[i] = hashes[i] + 1


    # hash with counters per letter 
    # 2 pointers 
    #   begin_window -> letter decrease counter 
    #   end_windown -> letter increase counter
    #   if all hashes == 0 bingo
    # start with filled hashes by "pattern"
    while begin_window < len(letters):
        print (end_window, begin_window,  hashes)

        hashes[letters[begin_window]] = hashes[letters[begin_window]] - 1
        if end_window >= 0:
            hashes[letters[end_window]] = hashes[letters[end_window]] + 1

        if all_is_zero(hashes):
            print ("!!!!!")
            found_patterns.append(end_window+1)

        begin_window = begin_window + 1
        end_window = end_window + 1
    
    return found_patterns


if __name__ == "__main__":
    #s = "cbaebabacd"
    #p = "abc"
    s = "abab"
    p = "ab"
    #s = "baa"
    #p = "aa"
    print(main(s, p))