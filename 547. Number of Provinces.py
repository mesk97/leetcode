# https://leetcode.com/problems/number-of-provinces/?envType=study-plan&id=algorithm-ii

# 547. Number of Provinces
# Medium
# 6.7K
# 277
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# 1 <= n <= 200

# list of cities 
# city is obj with links to others objs
# 1. move item by item -> create link between cities 
# 2. go city by citi and colour them 
# 3. coloring via stack 

class City:
    def __init__(self):
        self.color = None
        self.links = set()
        pass

def main(isConnected):
    number_of_provinces = 0
    number_of_cities = len(isConnected)
    cities = []
    for i in range(0, number_of_cities):
        cities.append(City())

    # crete graph
    for r in range(0, number_of_cities):
        for c in range(0, number_of_cities):
            if r == c:
                continue
            if isConnected[r][c]:
                cities[r].links.add(cities[c])
                cities[c].links.add(cities[r])

    # pass per city 
    for city in cities:
        if city.color is not None:
            continue

        number_of_provinces = number_of_provinces + 1
        color_to_mark = number_of_provinces

        stack = [city]
        #print(stack)
        while len(stack) > 0:
            item = stack.pop()
            #print ("item=", len(stack))
            item.color = color_to_mark
            for i in item.links:
                if i.color == None:
                    stack.append(i)

    return number_of_provinces

if __name__ == "__main__":
    #isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(main(isConnected))
