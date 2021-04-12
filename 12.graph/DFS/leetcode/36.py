''':cvar
조합의 합

숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
'''

# Output: [[2,2,3],[7]]
candidates = [2, 3, 6, 7]
target = 7


def solution(candidates, target):
    results = []

    def dfs(elements):

        if sum(elements) == target:
            results.append(elements[:])
            return

        for index in range(len(candidates)):
            dfs(candidates[index])

    dfs([])
    return results


print(solution(candidates, target))
