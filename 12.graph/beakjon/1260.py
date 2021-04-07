'''
예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4

예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
'''

graph = {}

import sys
from collections import deque

input: () = lambda: sys.stdin.readline().strip()
n, m, v = map(int, input().split())

count = 0
while m:
    if count == m:
        break
    key, value = map(int, input().split())
    if key not in graph:
        graph[key] = []
    if value not in graph:
        graph[value] = []
    graph[key].append(value)
    graph[value].append(key)
    count += 1

for g in graph:
    graph[g].sort()


def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = dfs(w, discovered)
    return discovered


def bfs(v):
    discovered = [v]
    dq = deque([v])
    while dq:
        v = dq.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                dq.append(w)
    return discovered


print(*dfs(v))
print(*bfs(v))
