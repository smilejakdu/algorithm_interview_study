''':cvar
[from , to] 로 구성된 항공권 목록을 이용해 JFK 에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘순 으로 방문한다.

Input : tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

'''

# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

import collections
from typing import List

# def solution(tickets):
#     graph = collections.defaultdict(list)
#     # 그래프 순서대로 구성
#     for a, b in sorted(tickets):
#         graph[a].append(b)
#
#     route = []
#
#     def dfs(a):
#         # 첫 번째 값을 읽어 어휘순 방문
#         while graph[a]:
#             dfs(graph[a].pop(0))
#         route.append(a)
#
#     dfs('JFK')
#     # 다시 뒤집어 어휘순 결과로
#     return route[::-1]
#
#
# print(solution(tickets))

''':cvar
pop() 은 O(1) 이지만 첫 번째 값을 꺼내는 pop(0) 은 O(n) 이다.
따라서 좀 더 효율적인 구현을 위해서는 pop()으로 , 즉 스택의 연산으로 처리 될 수 있도록 개션이 필요하다.
코드 크게 바뀌는거 없이 정렬할때 , reverse = True만 추가해서 graph[a].pop(0) 대신 graph[a].pop() 를 해주면 된다.
'''


def solution(tickets):
    graph = collections.defaultdict(list)
    # 그래프 뒤집어서 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 마지막 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘순 결과로
    return route[::-1]


print(solution(tickets))
