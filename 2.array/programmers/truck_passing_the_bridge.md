# 다리를 지나는 트럭

```
bridge_length	weight	truck_weights	                return
2	            10	    [7,4,5,6]	                    8
100	            100	    [10]	                        101
100	            100	    [10,10,10,10,10,10,10,10,10,10]	110
```

## 첫번째 풀이

```python
import collections


def solution(bridge_length, weight, truck_weights):
    queue = collections.deque([0] * bridge_length)
    truck_list = collections.deque(truck_weights)
    time = 0

    while queue:
        time += 1
        queue.popleft()
        if truck_list:
            if sum(queue) + truck_list[0] <= weight:
                queue.append(truck_list.popleft())
            else:
                queue.append(0)
    return time


print(solution(2, 10, [7, 4, 5, 6]))

```

## 두번째 풀이

```python
import collections


def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = collections.deque(truck_weights)
    l = len(trucks)
    bridge = collections.deque([0] * bridge_length)
    passed_trucks = collections.deque()
    total_weight = 0

    while True:
        if len(passed_trucks) == l:
            break

        item = bridge.popleft()
        if item != 0:
            total_weight -= item
            passed_trucks.append(item)
        bridge.appendleft()

        if bridge and not trucks:
            pass
        elif total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.pop()
            bridge.append(truck)
            total_weight += truck
        else:
            pass
        answer += 1

    return answer
```

## 세번째 풀이

```python



```
