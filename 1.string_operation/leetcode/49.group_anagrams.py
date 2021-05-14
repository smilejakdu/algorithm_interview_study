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
    string_list    = sorted(strs)
    string_list    = [''.join(sorted(string)) for string in string_list]
    string_diction = {}

    for string in string_list:
        if string not in string_diction:
            string_diction[string]=[]

    for string in strs:
        string_diction[''.join(sorted(string))].append(string)

    return list(string_diction.values())



# 답지 풀이

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams) # defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
    return list(anagrams.values())

print(groupAnagrams(Input))

