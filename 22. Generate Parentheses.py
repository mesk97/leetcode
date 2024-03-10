# https://leetcode.com/problems/generate-parentheses/?envType=study-plan&id=algorithm-ii
# 22. Generate Parentheses
# Medium
# 16.8K
# 666
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8


# logic:
#   есть функция parenthesis 
#       parenthesis[0] = ""
#       parenthesis[1] = "()"
#       parenthesis[n] = 
#       p[1]p[n-1] + p[2]p[n-2] + ... + p[n-1]p[1]
#   в функции есть results 
#       dict()  1 -> set(), 2 -> set()
#       set() -> позволяет убирать дупликаты
#  

results = dict()

def parentheses(n):
    global results
    if n in results:
        return results[n]

    results[n] = set()

    # process special case 
    previous = parentheses(n - 1)
    for p in previous:
        results[n].add("()" + p)
        results[n].add("(" + p + ")")
        results[n].add(p + "()")

    # process others 
    for i in range(2, n - 1):
        # mix results 
        left = parentheses(i)
        right = parentheses(n - i)

        for l in left:
            for r in right:
                results[n].add(l + r)
        
    return results[n]

def main(n):
    global results

    results[1] = set()
    results[1].add("()")
    
    return parentheses(n)

if __name__ == "__main__":
    n = 4
    print (main(n))
