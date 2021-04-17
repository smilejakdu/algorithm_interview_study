''':cvar
K 부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
불가능할 경우 -1 을 리턴한다.
입력 값 (u , v , w) 는 각각 출발지 , 도착지 , 소요 시간으로 구성되며 , 전체 노드의 개수는 N으로 입력받는다

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Example 4:
[[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
5
1
'''

times = [[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64], [1, 5, 54], [1, 4, 98], [2, 3, 61], [2, 1, 0],
         [3, 5, 77], [5, 1, 34], [3, 1, 79], [5, 3, 2], [1, 2, 59], [4, 3, 46], [5, 4, 44], [2, 5, 89], [4, 5, 21],
         [1, 3, 86], [4, 1, 95]]

n = 5
k = 1

import collections
import heapq


def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for 출발지, 도착지, 소요시간 in times:
        graph[출발지].append((도착지, 소요시간))

    # 큐 변수 : [(소요 시간 , 정점)]
    Q = [(0, k)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        정점, 간선 = heapq.heappop(Q)
        if 정점 not in dist:
            dist[정점] = 간선
            for 도착지, 소요시간 in graph[정점]:
                alt = 간선 + 소요시간
                heapq.heappush(Q, (alt, 도착지))

    # 모든 노드 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1


print(networkDelayTime(times, n, k))
