''':cvar
타로는 자주 JOI잡화점에서 물건을 산다.
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.
'''

import sys

N = int(sys.stdin.readline())
get_money = 1000 - N
num_list = [500, 100, 50, 10, 5, 1]
result = 0

while True:
    if get_money == 0:
        break
    if get_money >= 500:
        get_money = get_money - 500
    elif get_money >= 100:
        get_money = get_money - 100
    elif get_money >= 50:
        get_money = get_money - 50
    elif get_money >= 10:
        get_money = get_money - 10
    elif get_money >= 5:
        get_money = get_money - 5
    else:
        get_money = get_money - 1

    result += 1

print(result)

# 두번째 풀이

N = int(sys.stdin.readline())
get_money = 1000 - N
num_list = [500, 100, 50, 10, 5, 1]
result = 0
for num in num_list:
    result += get_money // num
    get_money %= num
print(result)
