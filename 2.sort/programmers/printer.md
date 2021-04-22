# 프린터

```
중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발
아래와 같은 방식으로 동작

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

priorities	        location	return
[2, 1, 3, 2]	    2	        1
[1, 1, 9, 1, 1, 1]	0	        5
```

## 첫번째 풀이

첫번째 드는 생각이 queue 로 풀어야겠단 생각을 했다.

queue 를 그냥 사용하기보단 deque 를 사용 하도록하자.

```python

import collections


def solution(priorities, location):
    queue = collections.deque(priorities)
    max_pri = max(priorities)
    count = 0

    while queue:
        if queue[0] == max_pri:
            break
        else:
            location -= 1
            count += 1
        queue.rotate(-1)
    return len(list(queue)[:location + 1])


print(solution([1, 1, 9, 1, 1, 1], 0))
```

일단 풀이를 이렇게 했는데 실행은 통과가 되는데 , 제출하게 되면 4개빼고 통과하지 못했다.

어디가 잘 못되었는지 감을 못잡겠다 ㅠㅠ

풀다가 다른 풀이를 봤다.

```python
import collections

def solution(priorities, location):
    queue = collections.deque(priorities)
    count = 0

    while len(queue) != 0:
        max_pri = max(queue)
        if location == 0:  # 출력 여부를 확인되는 맨 앞순서로 왔을 경
            if queue[0] < max_pri:  # 더 중요도 큰 문서가 있으면 
                queue.rotate(-1)  # 맨뒤로 간다.
                location = len(queue) - 1  # location 을 맨끝으로 설정 ( 배열길이 -1 )
            else:  # 더 우선순위가 높은 것이 없다면 내꺼가 출력되는 것이므로 return
                return count + 1
        else:
            if queue[0] < max_pri:
                queue.rotate(-1)
                location -= 1  # 맨앞 요소가 뒤로 갔기 때문에 location 이 1 줄어듦
            else:
                queue.popleft()  # 맨앞요소 출력됨
                location -= 1  # 맨앞 요소가 출력됐기 때문에 location 이 1 줄어듦
                count += 1  # (출력번째수 +1)


print(solution([1, 1, 9, 1, 1, 1], 0))
```

