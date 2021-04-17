times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

import collections
import heapq


def solution(times, n, k):
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))
    Q = [(0, k)]  # 경과 시간

    dist = collections.heapq(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    if len(dist) == n:
        return max(dist.values())

    return -1


print(solution(times, n, k))
