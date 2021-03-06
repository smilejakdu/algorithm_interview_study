'''
문자열 배열을 받아 에너그램 단위로 그룹핑 하라.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List
import collections
Input = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    string_list = sorted(strs)
    string_list = [''.join(sorted(string)) for string in string_list]
    string_list = collections.Counter(string_list)
    print(string_list)
    return

print(groupAnagrams(Input))


# 답지 풀이
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
