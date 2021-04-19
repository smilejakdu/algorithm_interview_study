''':cvar
동일한 값을 지닌 가장 긴 경로를 찾아라.

Example 1
Input: root = [5,4,5,1,1,5]
Output: 2
루트에서 오른쪽 노드 끝까지 5 -> 5 -> 5 로 가장 긴 이동 거리가 2이다.

Example 2
Input: root = [5,4,5,1,1,5]
Output: 2
왼쪽 리프 노드 4에서 형제 노드 4까지 4 -> 4 -> 4 로 가장 긴 이동 거리가 2이다.
'''

import collections


class TreeNode1(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode1(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


# lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
lst = [5, 4, 5, 1, 1, 5]
root = creatBTree(lst, 0)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


solution = Solution()
print(solution.longestUnivaluePath(root))
