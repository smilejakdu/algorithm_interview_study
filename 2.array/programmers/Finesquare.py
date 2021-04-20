'''
가로길이가 W
세로길이가 H

대각선으로 잘랐을때 정사각형 개수를 구하는 문제
W	H	result
8	12	80
'''


def solution(w, h):
    result = 0
    if (w + h) % 2 == 0:
        print('짝수')
        return w * h - max(w, h)
    else:
        print('홀수')

        return


print(solution(6, 2))
