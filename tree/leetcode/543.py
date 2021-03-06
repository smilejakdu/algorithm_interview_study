''':cvar
이진 트리에ㅏ서 두 노드 간 가장 긴 경로의 길이를 출력하라.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].

가장 긴 경로는 4 -> 2 -> 1 -> 3 또는 5 -> 2 ->1 -> 3 으로 3이다.

Example 2:
Input: root = [1,2]
Output: 1
'''


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
lst = [1, 2, 3, 4, 5]
root = creatBTree(lst, 0)


class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode2) -> int:
        print(root)

        def dfs(node: TreeNode2) -> int:
            # 리프노드의 left, right 노드를 None으로 초기화하므로 거기까지 타고 갔을때 -1을 리턴됨.
            if not node:
                return -1

            # 리프노트 다음 가상노드까지 끝까지 타고 들어감 ( 왼쪽, 오른쪽 각각 리프 노드까지 탐색 )
            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right)
            # 왼쪽, 오른쪽 상태값에 2를 더해서 거리를 구함. 기존 거리에 누적으로 max 값을 측정. ( 가장 긴 경로 )
            self.longest = max(self.longest, left + right + 2)

            # 아들 노드에 1더해서 상태값 리턴. ( 상태값 )
            return max(left, right) + 1

        dfs(root)

        return self.longest


solution = Solution()
print(solution.diameterOfBinaryTree(root))
