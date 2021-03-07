'''
덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

#nums   = [2,7,11,15]
#target = 9

nums   = [3,2,4]
target = 6

def twoSum(nums, target):

    for index in range(len(nums)):
        for index2 in range(len(nums)):
            if nums[index]+nums[index2] == target and index !=index2:
                return [index , index2]

print(twoSum(nums,target))



