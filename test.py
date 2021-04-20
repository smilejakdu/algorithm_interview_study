import sys
import collections


# N = int(sys.stdin.readline())
# a, b, c = map(int, sys.stdin.readline().split())

def solution(bridge_length, weight, truck_weights):
    queue = collections.deque([0] * bridge_length)
    truck_list = collections.deque(truck_weights)
    time = 0

    while queue:
        time += 1
        queue.popleft()
        if truck_list:
            if sum(queue) + truck_list[0] <= weight:
                queue.append(truck_list.popleft())
            else:
                queue.append(0)
    return time


print(solution(2, 10, [7, 4, 5, 6]))
