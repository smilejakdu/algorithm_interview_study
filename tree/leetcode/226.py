''':cvar

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

중앙을 기준으로 이진 트리를 반전시키는 문제이다.
이 문제는 맥


'''

import collections


# 첫번째 풀이
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None


''':cvar
두번째 풀이 BFS풀이
앞서 이진 트리의 최대 깊이 문제는 while 구문 내부에 별도의 for 문이 있어 부모 노드에 대해 따로 반복해야 했는데 ,
여기서는 그런 제약이 없이 자유롭게 스왑하면서 queue 에 추가한다.
먼저 삽입된 노드는 반복 구조로 계속 스왑되면서 자식 노드가 계속해서 큐에 추가되는 구조가 된다.

앞서 재귀 풀이가 가장 말단 , 리프 노드까지 내려가서 백트래킹하면서 스왑하는 상향 (Bottom-Up) 방식이라면 , 
이 풀이는 부모 노드부터 스왑함녀서 계속 아래로 내려가는 하향 (Top-Down) 방식 풀이라 할 수 있다.
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root


''':cvar
세번째 풀이
BFS 로 탐색할 때는 popleft() 로 처음 값을 추출했고 , 여기선 DFS 로 탐색할때는 pop() 으로 마지막 값을 추출했다.
변수명을 stack 으로 바꾼건 다소 그냥 형식적이다.
다만 , DFS 에서는 스택을 사용하고 실제로 pop() 만 사용했다는 점을 부각시키기 위해 변수명도 일부러 stack 으로 바꿔서 적용해봤다.
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root
