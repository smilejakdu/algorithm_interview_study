''':cvar
압력
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
출력
45

N+1 일째에는 회사에 없기 때문에 6 , 7 일에 있는 상담을 할 수 없다.
'''

import sys

num = int(sys.stdin.readline())
diction = {}

for i in range(1, num + 1):
    a, b = map(int, sys.stdin.readline().split())
    diction[i] = [a, b]

print("-" * 20)

for k, v in diction.items():
    print(k, v)


def solution():
    result = 0

    def dfs(index, ):
        for i, dic in enumerate(index, diction):
            print(i, dic)

        return

    dfs(1, )
    return


print(solution())
