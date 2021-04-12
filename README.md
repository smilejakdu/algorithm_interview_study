# algorithm_interview_study

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
