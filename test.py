import sys

# N = int(sys.stdin.readline())
# a, b, c = map(int, sys.stdin.readline().split())

import collections

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge(intervals):
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):  # [[1, 3], [2, 6], [8, 10], [15, 18]]
        # 첫번재 값을 기준으로 정렬을 해준다. 즉  1 , 2 , 8 , 15 를 정렬한다.
        if merged and i[0] <= merged[-1][1]:  # 다음 아이템의 시작이 <= 이전아이템 끝보다 작거나 같다면
            merged[-1][1] = max(merged[-1][1], i[1]) # 이전아이템 끝 = max( 이전아이템 끝 , 다음아이템끝 )
        else:
            merged += i,  # 콤마를 넣게 되면 중첩 리스트를 만들어 준다. merged += [i] 와 같다.
    return merged


print(merge(intervals))
