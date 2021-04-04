import sys
graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7:[3],
}
discovered = []

def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)
  return discovered


print(recursive_dfs(1))


# DFS 두번째 예제 


input: () = lambda: sys.stdin.readline().strip()

# n, m = map(int, input().split())
n, m = 4, 2
used = [False] * n  # 탐사 여부 check
result = []  # 출력 내용


def solve(depth, n, m):
    if depth == m:  # 탈출 조건
        print(*result)  # list를 str으로 합쳐 출력
        return
    for i in range(n):  # 탐사 check 하면서
        if not used[i]:  # 탐사 안했다면
            used[i] = True  # 탐사 시작(중복 제거)
            result.append(i + 1)  # 탐사 내용
            solve(depth + 1, n, m)  # 깊이 우선 탐색
            used[i] = False  # 깊이 탐사 완료
            result.pop()  # 탐사 내용 제거


print(solve(0, n, m))
