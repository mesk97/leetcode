# https://leetcode.com/problems/redundant-connection/description/
# 18.06
# 18.18  - написал первыую версию .. запустил и осознал что задача сложнее 

# 21 / 39 testcases passed
# edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
# Output [6,8]
# Expected [4,10]

# 21 / 39 testcases passed
# edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
# Use Testcase Output []
# Expected [2,5]


# Runtime
# 61
# ms
# Beats
# 27.94%
# of users with Python3
# Memory
# 17.21
# MB
# Beats
# 21.51%
# of users with Python3


# 684. Redundant Connection
# Medium
# Topics
# Companies
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# Accepted
# 348.9K
# Submissions
# 555.8K
# Acceptance Rate
# 62.8%
# Topics
# Depth-First Search
# Breadth-First Search
# Union Find
# Graph

def main(edges):
    stats = dict()
    result = []

    for e in edges:
        cloud0 = set()
        cloud1 = set()
        if e[0] in stats:
            cloud0 = stats[e[0]]
            if e[1] in cloud0:
                result = e
        if e[1] in stats:
            cloud1 = stats[e[1]]
            if e[0] in cloud1:
                result = e
        
        cloud0.update(cloud1)
        cloud0.update(e)
        stats[e[0]] = cloud0
        stats[e[1]] = cloud0

        for i in cloud1:
            stats[i] = cloud0

    return result

if __name__ == "__main__":
    edges = [[1,2],[1,3],[2,3]]
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
    edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    print(main(edges))