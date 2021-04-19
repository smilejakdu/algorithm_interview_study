# algorithm_interview_study

# 알고리즘 공부 순서

1. 그리디 알고리즘(탐욕적인 알고리즘)
2. 탐색(완전탐색 , BFS , DFS)
3. 기본 동적 프로그래밍 (DP)

그리디 , 기본 동적 프로그래밍 , 탐색문제 각각 최소한 100문제씩 각각 풀고 화 시키기 


## input 데이터 받기

```python
import sys

T = int(input()) 
for i in range(T):
    a , b = map(int , sys.stdin.readline().split())
```

## 여러 정수를 한줄로 입력받기 

```python
import sys
a,b,c = map(int , sys.stdin.readline().split())
```

## sys.stdin.readline() 

```python
import sys
a = int(sys.stdin.readline())
```

## 문자열 n 줄을 입력받아 리스트에 저장할 때

```python
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

# 문제 질문 방법

```
문제 : https://www.acmicpc.net/problem/20061
코드 : http://colorscripter.com/

백준 20061 모노미노도미노 2 입니다.
테케, 질문에서 찾은 반례 모두 맞고
테케 설명에 있는 대로 남은 타일의 갯수 뿐만 아니라 위치까지 정확히 계산됩니다.
하지만 제출시 틀렸습니다 가 떠서 질문드립니다
반례 또는 특정 함수를 지적해 주시면 해당부분 다시 구현해 보겠습니다
```
