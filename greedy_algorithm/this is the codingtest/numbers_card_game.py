''':cvar
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단 , 게임의 룰을 지키며 카드를 뽑아야 한다.

1. 숫자가 쓰인 카드는 N x M 형태  ( N 은 행 , M 은 열)
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.

입력 예시 1
3 3
3 1 2
4 1 4
2 2 2
출력 예시 1
2

입력 예시 2
2 4
7 3 1 8
3 3 3 4
출력 예시 2
3
'''

# 나의풀이
import sys

N, M = map(int, sys.stdin.readline().split())
min_list = []

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    min_list.append(min(i))
print(max(min_list))

# 정답 풀이 1
n, m = map(int, input().split())
result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
