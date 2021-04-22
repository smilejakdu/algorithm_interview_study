# 스킬트리

```
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 말한다.
하지만 순서에 없는 다른 스킬은 순서에 상관없이 배울 수 있다.

따라서 ,
스파크 -> 힐링 -> 라이트닝 볼트 -> 썬더 와 같은 스킬트리는 가능하지만,
썬더 -> 스파크 
라이트닝 볼트 -> 스파크 -> 힐링 -> 썬더 
와 같은 스킬트리는 불가능하다.

```

```python
def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees: # BACDE
        user_sk = [ s for s in st if s in skill ]
        if skill.startswith(''.join(user_sk)):
            answer += 1

    return answer
```

