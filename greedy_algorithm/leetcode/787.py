''':cvar
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되 , K 개의 경유지 이내에 도착하는 가격을 리턴하라.
경로가 존재하지 않을 경우 -1 을 리턴한다.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
'''

import collections
import heapq

n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]  # [시작점 , 도착점 , 비용]
src, dst, k = 0, 2, 1


# 시작점 , 도착점 , 경유지
# Output: 200

def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, K)]  # ( 가격 , 정점 , 남은 가능 경유지 수 )

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


print(findCheapestPrice(n, edges, src, dst, k))


# 두번째 풀이


def findCheapestPrice(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    k = 0
    Q = [(0, src, K)]  # ( 가격 , 정점 , 남은 가능 경유지 수 )

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= K:
            k += 1
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k))
    return -1


print(findCheapestPrice(n, edges, src, dst, k))
