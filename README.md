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


