''':cvar
모든 부분 집합을 리턴하라.
nums = [1, 2, 3]

[
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
]
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
nums = [1, 2, 3]


def subsets(nums):
    result = []

    def dfs(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


print(subsets(nums))

''':cvar
이문제를 보는순간 어떻게 풀어야할지 보였고 , 눈물이 나왔다.
'''