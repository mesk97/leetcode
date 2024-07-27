# https://leetcode.com/problems/restore-ip-addresses/description/

# 93. Restore IP Addresses
# Medium
# Topics
# Companies
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits only.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 471.8K
# Submissions
# 932.5K
# Acceptance Rate
# 50.6%
# Topics
# String
# Backtracking

# Algo
# идем по строке
# кладем в стэк 
#     IPtoConstruct - начинаем с ""
#     строку 
# берем в цикле из стэка пока не пустой
# есть несколько вариантов
# 1. добавляем к IP следующую цифру
#     если валидно 
#       строка кончилась -> записываем
#        строка не кончилась - кладем в стэк
#     если не валидно и можно продолжать -> в стэк
#     если не валидно и нельзя продолжать -> стоп цепочку
# 2. добавляем точку
#     если не валидно и можно продолжать -> в стэк
#     если не валидно и нельзя продолжать -> стоп


# Runtime
# 65
# ms
# Beats
# 8.93%
# Analyze Complexity
# Memory
# 16.63
# MB
# Beats
# 15.88%

    
def addNumber2IP(ip, d):
    ip = ip.copy()
    if len(ip) == 0:
        ip.append(None)
    octet = ip[-1]

    if octet is None:
        ip[-1] = d
        return ip
        
    if octet == 0:
        return None
    
    octet = octet * 10 + d
    if octet > 255:
        return None
    
    ip[-1] = octet
    return ip
    
def addDot2IP(ip):
    if len(ip) == 0 or ip[-1] is None:
        return None
    ip = ip.copy()
    ip.append(None)
    return ip

def main(s):
    stack = []
    result = []
    
# идем по строке
# кладем в стэк 
#     IPtoConstruct - начинаем с ""
#     строку 
    # IP, str
    ip = []
    item = (ip, s)
    stack.append(item)

# берем в цикле из стэка пока не пустой
    while len(stack) > 0:
        (ip, s) = stack.pop()

        if len(s) == 0:
            if len(ip) == 4 and not ip[-1] is None:
                result.append('.'.join(str(num) for num in ip))
            continue

# есть несколько вариантов
# 1. добавляем к IP следующую цифру
        ip1 = addNumber2IP(ip, int(s[0]))
        if not ip1 is None:
            stack.append((ip1, s[1:])) 

# 2. добавляем точку
        ip2 = addDot2IP(ip)
        if not ip2 is None:
            stack.append((ip2, s))      

    return result

if __name__ == "__main__":
    s = "101023"
    print(main(s))