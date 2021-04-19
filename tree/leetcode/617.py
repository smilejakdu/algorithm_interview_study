''':cvar
두 이진 트리를 벼합하라 .
중복되는 노드는 값을 합산한다.

Example 1 )
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2 )
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergegeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2
