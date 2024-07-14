# https://leetcode.com/problems/longest-palindromic-substring/description/

# 5. Longest Palindromic Substring
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.2M
# Submissions
# 9.2M
# Acceptance Rate
# 34.1%
# Topics
# Two Pointers
# String
# Dynamic Programming

# алго
# запоминаем максималку  + индекс I начало последнего палиндрома
# если текущее Т == I-1 то 
# I = I - 1
# иначе 
# максималка = макс (максималка, len (от I до Т))
# I = Т
# еще добавдяем вначале и в конце по спец симвллу чтобы края не отрабатывать 

# 132 / 142 testcases passed
# Input
# s =
# "bananas"
# Output
# "ana"
# Expected
# "anana"


def main(s):
    max_len = 0
    max_str = ""
    special_case = None

    index_pal = 1
    # еще добавдяем вначале и в конце по спец симвллу чтобы края не отрабатывать
    # разные чтобы не натыкаться на палиндром с _ 
    str = "_" + s + ":"

    for index_current in range(1, len(str)):
        if str[index_current] == str[index_pal - 1]:
            index_pal = index_pal - 1
            continue

        # спец случай  s = "cbbad"
        if index_current > index_pal and str[index_current] == str[index_pal]:
            if (index_current - index_pal) > 1:  # это для обработки единичных
                if str[index_current] == special_case:
                    continue
                special_case = None
            else:
                special_case = str[index_current]
                continue
        else:
            special_case = None

        new_len = index_current - index_pal
        if new_len > max_len:
            max_len = new_len
            max_str = str[index_pal:index_current]
        index_pal = index_current

    return max_str

if __name__ == "__main__":
    s = "babad"
    s = "ba"
    s = "cbbbbabd"
    s = "ddddddd"
    s = "bananas"
    print(main(s))