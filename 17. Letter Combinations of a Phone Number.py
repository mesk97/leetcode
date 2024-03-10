# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan&id=algorithm-ii
# 17. Letter Combinations of a Phone Number
# Medium
# 14K
# 808
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Item:
    def __init__(self, digits, seq):
        self.digits = digits
        self.seq = seq
        pass

def main(digits):
    results = []
    stack = []
    phones = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }    

    if (len(digits) > 0):
        stack.append(Item(digits, ""))

    while len(stack) > 0:
        item = stack.pop()
        digit = item.digits[0]
        next_digits = item.digits[1:]
        seq = item.seq

        for letter in phones[digit]:
            new_seq = seq + letter
            
            if len(next_digits) == 0:
                results.append(new_seq)
                continue

            stack.append(Item(next_digits, new_seq))

    return results

if __name__ == "__main__":
    digits = "23"
    print(main(digits))