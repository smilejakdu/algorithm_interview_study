# 첫번째풀이

import re

#Input = 'race a car'
Input = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    string = s.lower()
    string = re.sub("[^a-z0-9]","",string)
    result_string = string[::-1]
    result = True if result_string == string else False
    return result

print(isPalindrome(Input))

# 두번째 문제 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


# 세번째 문제풀이
import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

# 네번째 문제풀이

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱
    
# 슬라이싱
s[1:4]  == 녕하세
s[1:-2] == 녕하
#인덱스 1에서 -2이전까지 표현한다.
s[1:]   == 녕하세요
s[:]    == 안녕하세요
s[-1]   == 요
s[-4]   == 녕
#뒤에서 4번째
s[:-3]  == 안녕
#뒤에서 3개 글자 앞까지
s[-3:]  == 하세요
#뒤에서 3번째 문자에서 마지막까지
s[::1]  == 안녕하세요
s[::-1] == 요세하녕안
s[::2]  == 안하요
#2칸씩 앞으로 이동
