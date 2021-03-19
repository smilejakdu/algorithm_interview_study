'''
T = [73,74,75,71,69,72,76,73]
'''

T = [73,74,75,71,69,72,76,73]

from typing import List

def solution(T : List[int])->List[int]:
    answer = [0]*len(T)
    stack  = [] # [ 0 ]

    for i , cur in enumerate(T): # 1 , 74
        # 현재 온도가 스택 값보다 높다면 정답처리
        while stack and cur > T[stack[-1]]: # 74 > 73
            last = stack.pop() # 0
            answer[last] = i - last # answer[0] =1
        stack.append(i) 

    return answer

print(solution(T))

# 다른풀이

def dailyTemperatures(self, T):
    ans   = [0] * len(T)
    stack = [] #indexes from hottest to coldest
    
    for i in xrange(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans
