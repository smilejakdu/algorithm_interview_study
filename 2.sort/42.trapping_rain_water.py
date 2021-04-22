'''
높이를 입력받아 비 온후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right] # 왼쪽 끝 , 오른쪽 끝

    while left < right:
        left_max, right_max = max(height[left], left_max) , max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

print(trap(height))
