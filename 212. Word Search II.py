# https://leetcode.com/problems/word-search-ii/description/

# algo:
# 0. с words строим TrieNode(..)
# 1. есть стэк с  tuple=(TrieNode(char), x, y)
# 2. проходим всю матрицу и впихиваем живые tuple
# 3. идем по стэку если  
#            TrieNode(char) конечная -> успех
#            от ячейки по направлениям есть символ и он в TrieNode(char+1) то впихиваем в стэк
# 4. пока не кончится 

# 212. Word Search II
# Hard
# Topics
# Companies
# Hint
# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

# Example 1:


# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:


# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 631.9K
# Submissions
# 1.7M
# Acceptance Rate
# 36.2%
# Topics
# Array
# String
# Backtracking
# Trie
# Matrix

# trial 1:  30 / 65 testcases passed
# не учел что слово может быть и final и содержать 
# trial 2:  55 / 65 testcases passed
# не учел переиспользование одной и той же буквы 
# trial 3: 47 / 65 testcases passed
# хмм стало ломаться что то еще  - кэш использования криво работал 
# trial 4: 53 / 65 testcases passed
#  еще один фэйл кэша использования
# trial 5: 62 / 65 testcases passed
# ... опять кэш использования - но непонятно как 

class TrieNode:
    def __init__(self, symbol = None):
        self.final = 0
        self.symbol = symbol
        self.next = dict()

    # def link()

    #     #self.next = [ None ] * (ord('z') - ord('a') + 1)
    #     if str is None or len(str) == 0:
    #         return
    #     self.symbol = str[0]
    #     newstr = str[1:]
    #     if len(newstr) == 0:
    #         self.final = 1

    #     next = TrieNode(newstr)
    #     self.link(self.symbol, next)
    #     return
    
    def link(self, symbol, node):
        item = node
        if symbol in self.next:
            item = self.next[symbol]
        else:
            self.next[symbol] = node
        return item
    
    def setFinal(self):
        self.final = 1

    def isFinal(self):
        #return len(self.next) == 0
        return self.final
    
    def getNext(self, symbol):
        if symbol in self.next:
            return self.next[symbol]
        return None

def check(node, x, y, board, board_x_len, board_y_len, stack, result, word, used_symbols):
    if x < 0 or y < 0 or x >= board_x_len or y >= board_y_len:
        return
    
    char = board[y][x]

    # уже использовали
    if (x, y) in used_symbols:
        print(x, y, char, word)
        return
    

    next = node.getNext(char)
    if next is None:
        return
    
    word = word + char
    if next.isFinal():
        result.add(word)
        #return

    used_symbols = used_symbols.copy()
    used_symbols.add((x, y))
    stack.append((next, x, y, word, used_symbols))

def main(board, words):
    result = set()

    board_y_len = len(board)
    board_x_len = len(board[0])

    # установим TrieNode-ы
    root = TrieNode()
    for w in words:
        tolink = root
        for i in range(0, len(w)):
            item = TrieNode(w[i])
            tolink = tolink.link(w[i], item)
        tolink.setFinal()

    # 1. есть стэк с  tuple=(TrieNode(char), x, y)
    # 2. проходим всю матрицу и впихиваем живые tuple
    # 3. идем по стэку если  
    #            TrieNode(char) конечная -> успех
    #            от ячейки по направлениям есть символ и он в TrieNode(char+1) то впихиваем в стэк
    # 4. пока не кончится
    stack = []

    # инитим стартовые точки 
    for y in range(0, board_y_len):
        for x in range(0, board_x_len):
            check(root, x, y, board, board_x_len, board_y_len, stack, result, '', set())

    cache = set()
    while len(stack) > 0:
        (node, x, y, word, used_symbols) = stack.pop()

        # ускоряем
        if (node, x, y, word) in cache:
            continue
        cache.add((node, x, y, word))

        # проверяем
        check(node, x+1, y, board, board_x_len, board_y_len, stack, result, word, used_symbols)
        check(node, x, y+1, board, board_x_len, board_y_len, stack, result, word, used_symbols)
        check(node, x-1, y, board, board_x_len, board_y_len, stack, result, word, used_symbols)
        check(node, x, y-1, board, board_x_len, board_y_len, stack, result, word, used_symbols)

    return list(result)

if __name__ == "__main__":
    board = [
             ["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]
            ]
    words = ["oath","pea","eat","rain"]

    #board = [["a","b"],["c","d"]]
    #words = ["abcb"]

    # board = [
    #     ["o","a","b","n"],
    #     ["o","t","a","e"],
    #     ["a","h","k","r"],
    #     ["a","f","l","v"]
    # ]
    # words = ["oa","oaa"] 

    # board = [["a","a", "a"]]
    # words = ["aaa"]

    board =[
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
        ]
    words = ["oath","pea","eat","rain","hklf", "hf"]
    # Output   ["oath","hf","eat"]
    # Expected ["oath","eat","hklf","hf"]

    board = [
        ["a","b","c"],
        ["a","e","d"],
        ["a","f","g"]
        ]
    words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
    # Output   ["gfedcbaaa","befa","abcdefg"]
    # Expected ["gfedcbaaa","befa","abcdefg","eaabcdgfa"]

    board = [
        ["d","c","e","b","d","e","d","a"],
        ["c","a","e","a","d","d","e","e"],
        ["a","c","e","d","b","c","c","b"],
        ["c","b","a","a","a","e","e","e"],
        ["a","e","d","e","b","d","d","e"],
        ["a","a","d","c","e","a","d","e"],
        ["b","d","e","b","b","b","c","e"],
        ["d","a","e","e","b","e","b","d"],
        ["b","b","c","a","b","b","b","a"],
        ["a","c","b","a","c","a","d","d"]]
    words = ["ab","bddbebcba","ededa","daebeda","edecaeabc","cbeedad","bcaaecb",
             "c","eb","aadbdbacee","dcaaba"]
    # Output   ["eb","c","ab","daebeda"]
    # Expected ["eb","c","ab","daebeda","ededa"]

    print (main(board, words))