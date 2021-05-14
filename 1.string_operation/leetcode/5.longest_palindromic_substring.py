'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''

Input = "cazdanaddsewac"
def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
        print(i , Input[i] , Input[i+1] , Input[i+1] , result)
    return result

# 다른 풀이
#class Solution:
#    def longestPalindrome(self, s):
#        """
#        :type s: str
#        :rtype: str
#        """
#        # Return if string is empty
#        if not s: return s
#
#        res = ""
#        for i in range(len(s)):
#            j = i + 1
#            # While j is less than length of string
#            # AND res is *not* longer than substring s[i:]
#            while j <= len(s) and len(res) <= len(s[i:]):
#                # If substring s[i:j] is a palindrome
#                # AND substring is longer than res
#                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
#                    res = s[i:j]
#                j += 1
#
#        return res
#
print(longestPalindrome(Input))
