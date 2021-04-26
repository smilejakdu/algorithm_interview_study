import sys

# N = int(sys.stdin.readline())
# a, b, c = map(int, sys.stdin.readline().split())

import collections
from typing import List

# nums = [10, 2]
nums = [3, 30, 34, 5, 9]
from typing import List


class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)  # 거꾸로 했을때 값이 더 크면 true ex ) 102 < 210

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):  # i 가 리스트 길이보다 작다면
            j = i  # j 라는 변수에 넣는다.
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):  # j 가 0 보다 크고 to_swap(nums[j-1] , nums[j]) 가 true 이면
                nums[j], nums[j - 1] = nums[j - 1], nums[j]  # swap 을 한다.
                j -= 1  # j 가 1씩 작아진다.
            i += 1  # i 가 1씩 커진다

        return str(int(''.join(map(str, nums))))


solution = Solution()
print(solution.largestNumber(nums))
