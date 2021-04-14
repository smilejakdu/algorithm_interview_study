''':cvar
'큰수의 법칙'
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰수를 만드는 법칙이다.
단 , 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이법칙의 특징이다.

예를들어
배열 : [2 , 4 , 5 , 4 , 6]
M : 8
K : 3

이러한 경우 특정한 인덱스의 수가 연속해서 3 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46
'''
# 나의 풀이
import sys

list_length, n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count, k_count, result = 0, 0, 0
nums.sort()
first, second = nums[-1], nums[-2]
while True:
    if count == n:
        break
    if k_count != k:
        result += first
    else:
        result += second
        k_count = 0
    count += 1
    k_count += 1
print(result)

# 다른 풀이

''':cvar
이 문제는 전형적인 그리디 알고리즘 문제이다.
이 문제를 해결하려면 일단 입력 값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복한다.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 두번째 풀이
''':cvar
가장 큰수 : 6
두번째로 큰수 : 5

이때 M 이 8 , K 가 3 이라면 
(6+6+6+5)+(6+6+6+5) = 46
반복되는 수열에 대해서 파악
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  # 가장 큰 수가 등장하는 횟수
count += m % (k + 1)  # 나누어 떨어지지 않는 경우도 고려

result = 0
result += count * first
result += (m - count) * second

print(result)
