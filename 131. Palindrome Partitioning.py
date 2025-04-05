# https://leetcode.com/problems/palindrome-partitioning/description/
# 131. Palindrome Partitioning
# Medium
# Topics
# Companies
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.
# Accepted
# 954.1K
# Submissions
# 1.4M
# Acceptance Rate
# 70.2%
# Topics
# String
# Dynamic Programming
# Backtracking


# алго
# 1. d[x] += все d[x-1] partitions + добавляем 'x' как отдельный элемент
# 2. если s[-2] = s[-1] то d[x-2] partitions + добавляем 'xx' как отдельный элемент
# 3. находим назад все встречания 'x' -3,-4,-5 ... 
#     проверяем все d[x-1]  и если там partition[-2] = 'x' 
#       то берем d[x - len(partition[-1])] partitions и добавляем 'x' partition[-1] 'x' элемент

def find_symbol_occurrences(input_string, symbol):
    occurrences = []
    for index, char in enumerate(input_string):
        if char == symbol:
            occurrences.append(index)
    return occurrences

def D(s):
    global cache
    partitions = []

    print("D in '" + s + "'")

    if s in cache:
        print("D out '" + s + "' cache: ", cache[s])

        return cache[s]

    last_symbol = s[-1]

    # 1. d[x] += все d[x-1] partitions + добавляем 'x' как отдельный элемент
    minus1_partitions = D(s[:len(s)-1])
    for p in minus1_partitions:
        p.append(last_symbol)
        partitions.append(p)

    # 2. если s[-2] = s[-1] то d[x-2] partitions + добавляем 'xx' как отдельный элемент
    if s[-2] == last_symbol:
        double_last_symbol = last_symbol + last_symbol
        minus2_partitions = D(s[:len(s)-2])
        for p in minus2_partitions:
            p.append(double_last_symbol)
            partitions.append(p)

    # 3. находим назад все встречания 'x' -3,-4,-5 ... 
    #     проверяем все d[x-1]  и если там partition[-2] = 'x' 
    #       то берем d[x - len(partition[-1])] partitions и добавляем 'x' partition[-1] 'x' элемент
    s_minus_3 = s[:-3]
    for index in find_symbol_occurrences(s_minus_3, last_symbol):

        for p in minus1_partitions:
            if minus1_partitions[-2] != last_symbol:
                continue
            last_symbol_palindrome = last_symbol + minus1_partitions[-1]  + last_symbol
            p3_partitions = D(s[:index])
            for p in p3_partitions:
                p.append(last_symbol_palindrome)
                partitions.append(p)

    # убрать не уникальные 

    # записать в кэш

    print("D out '" + s + "': ", partitions)

    return partitions

def main(s):
    global cache
    cache = dict()

    # добавляем часть спецслучаев
    cache[''] = []
    cache[s[0]] = [[s[0]]]
    if len(s) > 1 and s[0] == s[1]:
        cache[s[0:2]] = [[ s[0], s[1] ], [s[0:2]]]

    print(cache)

    return D(s)

if __name__ == "__main__":
    s = "aaa"
    print(main(s))