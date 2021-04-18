class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


# lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
# root = creatBTree(lst, 0)
