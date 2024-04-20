# https://leetcode.com/problems/task-scheduler/description/
# 10.46
# 14 / 71 testcases passed -> забыл про то по какому приоритету вытаскивают

# Runtime
# 1167
# ms
# Beats
# 5.01%
# of users with Python3
# Memory
# 17.28
# MB
# Beats
# 27.96%
# of users with Python3

# algo
# 0. есть "0 priority queue" - откуда берем при запуске 
#    и массив из "1 .. N priority queu"
# 1. проходим все таски формируем 0 priority_queue
# 2. состав A:5, B:4, C:3 -> чем больше тасок такого типа тем больше приоритет
# 3. контролируем сколько всего тасок осталось 
# 4. цикл до окончания тасок 
# 5. берем первую в "0 prioriy queue"
# 6. если там нет - то +1 к idle
# 7. смещаем на 1 приорити очередь  1-> 0 ... N -> N-1
# 8. выбраную таску помещаем в "N priority queue"

# 621. Task Scheduler
# Medium
# Topics
# Companies
# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

# Constraints:

# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 514.7K
# Submissions
# 882.8K
# Acceptance Rate
# 58.3%
# Topics
# Array
# Hash Table
# Greedy
# Sorting
# Heap (Priority Queue)
# Counting

import collections
import queue

def main(tasks, n):
    # очередь на исполнение 
    runq = queue.PriorityQueue()

    # сетап runq
    setup = dict()
    for t in tasks:
        if not t in setup:
            setup[t] = 0
        setup[t] = setup[t] + 1
    for (k, v) in setup.items():
        runq.put((-v, k))

    # создаем и инитим waitq - очередь ожидания
    waitq = collections.deque()
    for i in range(n):
        waitq.append(None)
    
    executed_num = 0
    tasks_num = len(tasks)

    while tasks_num > 0:
        executed = None
        executed_num = executed_num + 1

        # определяем есть ли таски 
        if not runq.empty():
            # вытаскиваем задачи с максимумом num на execution
            (num, task_type) = runq.get()
            # экзекьютим
            tasks_num = tasks_num - 1
            num = num + 1
            if num < 0:
                executed = (num, task_type)

        # вставляем в конце
        waitq.append(executed)
        
        # rotate waitq - вытаскиваем кто уже отсидел idle
        item = waitq.popleft()
        if not item is None:
            runq.put(item)

    return executed_num

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2

    #tasks = ["A","C","A","B","D","B"]
    #n = 1

    #tasks = ["A","B","A"]
    #n = 2
    #Output 5
    #Expected 4

    print (main(tasks, n))