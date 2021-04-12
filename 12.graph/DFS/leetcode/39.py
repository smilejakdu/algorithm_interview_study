''':cvar
숫자 집합 candidates 를 조합하여 합이 target 이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


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


사실 이문제는 DFS 로 풀지않아도 풀수는 있지만 , DFS 로 풀어보도록 하자 .
'''

# candidates = [2, 3, 6, 7]
# target = 7

candidates = [2, 3, 5]
target = 8


# 하나씩 빼면서 result 에 추가하는 방

def combinationSum(candidates, target):
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0: return
        if csum == 0:
            result.append(path)
            return

        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


print(combinationSum(candidates, target))


# 하나씩 더해서 result 에 추가하는 방법
def combinationSum(candidates, target):
    result = []

    def dfs(index, path):
        if sum(path) == target:
            result.append(path)
            return
        elif sum(path) > target:
            return

        for i in range(index, len(candidates)):
            dfs(i, path + [candidates[i]])

    dfs(0, [])
    return result


print(combinationSum(candidates, target))
