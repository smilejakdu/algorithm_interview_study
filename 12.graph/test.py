graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7: [3],
}

def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)
  return discovered

print(recursive_dfs(1))
      