''':cvar
n = 4,
k = 2

출력
[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4]
]
'''
n = 4
k = 2


def solution(n, k):
    results = []

    def dfs(index, elements):
        if len(elements) == k:
            results.append(elements[:])
            return

        for i in range(index, n + 1):
            elements.append(i)
            dfs(i + 1, elements)
            elements.pop()

    dfs(1, [])

    return results


print(solution(n, k))
