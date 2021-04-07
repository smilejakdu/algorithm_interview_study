'''
순열
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''
from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

print(permute([1,2,3]))