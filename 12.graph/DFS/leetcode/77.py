''':cvar
전체 수 n을 입력받아 k개의 조합을 리턴하라.
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
조합이란 ??

'''

n = 4
k = 2


def combine(n, k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


print(combine(n, k))


# 두번째 풀이

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
