# Binary search
# https://leetcode.com/problems/time-based-key-value-store/
# 981. Time Based Key-Value Store
# Medium
# Topics
# Companies
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 398.2K
# Submissions
# 799.8K
# Acceptance Rate
# 49.8%
# Topics
# Hash Table
# String
# Binary Search
# Design

# 20:45
# 21:29 -> fail

class TimeMap:
    def __init__(self):
        self.treemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        main_set(self.treemap, key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        return main_get(self.treemap, key, timestamp)


def search(timestamps, t):
    begin_index = 0
    end_index = len(timestamps) - 1

    # обработаем краевые случае
    if t >= timestamps[end_index]:
        return end_index
    if t < timestamps[begin_index]:
        return None

    while ((end_index - begin_index) >= 2):
        middle = int((end_index + begin_index)/2)
        if timestamps[middle] <= t:
            begin_index = middle
        else:
            end_index = middle    
    return begin_index

def main_set(treemap, key, value, timestamp):
    if not key in treemap:
        treemap[key] = dict()
        treemap[key]['t'] = []
        treemap[key]['v'] = []
    treemap[key]['t'].append(timestamp)
    treemap[key]['v'].append(value)
    return 

def main_get(treemap, key, timestamp):
    if not key in treemap:
        return ''
    index = search(treemap[key]['t'], timestamp)
    if index is None:
        return ''
    return treemap[key]['v'][index]

def main(functions, values):
    timeMap = TimeMap()
    result = []
    for i in range(0, len(functions)):
        v = values[i]
        if functions[i] == "set":
            timeMap.set(v[0], v[1], v[2])
        else:
            result.append(timeMap.get(v[0], v[1]))
    return result

if __name__ == "__main__":
#    functions = ["set", "get", "get", "set", "get", "get"]
#    values = [["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    functions = ["set","set","get","get","get","get","get"]
    values = [["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

    print (main(functions, values))
    