''':cvar
N 이 1이 될때까지 다음 두과정 중 하나를 반복적으로 수행한다.
1. N 에서 1 을 뺀다
2. N 을 K 로 나눈다.

example 1 )
input
25 5
output
2
'''
import sys

n, k = map(int, sys.stdin.readline().split())
# count = 0
# while True:
#     if n % k == 0:
#         n = n // k
#         count += 1
#     else:
#         n -= 1
#         count += 1
#     if n == 1:
#         break
# print(count)

# 다른 풀이

''':cvar
아래와 같이 풀게 되면 시간 복잡도가 log 가 나오기때문에 다시한번 이해하기를 바람
'''

result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)
