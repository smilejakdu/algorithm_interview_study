graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

from collections import deque

deq = deque(['a', 'b', 'c'])


def iterative_bfs(start_v):
    discovered = [start_v]
    dq = deque([start_v])
    while dq:
        v = dq.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                dq.append(w)
    return discovered


print(iterative_bfs(1))  # [1, 2, 3, 4, 5, 6, 7]
