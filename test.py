import sys

# N = int(sys.stdin.readline())
# a, b, c = map(int, sys.stdin.readline().split())

import collections


def solution(priorities, location):
    queue = collections.deque(priorities)
    count = 0

    while len(queue) != 0:
        max_pri = max(queue)
        if location == 0:
            if queue[0] < max_pri:
                queue.rotate(-1)
                location = len(queue) - 1
            else:
                return count + 1
        else:
            if queue[0] < max_pri:
                queue.rotate(-1)
                location -= 1
            else:
                queue.popleft()
                location -= 1
                count += 1


print(solution([1, 1, 9, 1, 1, 1], 0))
