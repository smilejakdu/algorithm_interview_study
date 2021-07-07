from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        linklist_to_list = self.toList(head)
        len_linklist_to_list = len(linklist_to_list)
        if len_linklist_to_list % 2 == 0:
            front = linklist_to_list[:len(linklist_to_list) // 2]
            back = linklist_to_list[len(linklist_to_list) // 2:]
            result = sorted(front, reverse=True) + sorted(back, reverse=True)
            return self.toReversedLinkedList(result)
        else:
            front = linklist_to_list[:len(linklist_to_list) // 2]
            back = linklist_to_list[len(linklist_to_list) // 2 + 1:]
            sorted(front) + sorted(back)
        print(front)
        print(back)

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: List) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node


def printAll(head):
    result_list = []
    start = head

    while start:
        result_list.append(start.val)
        start = start.next
    print(result_list)


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
# l1_5 = ListNode(5)
# l1_6 = ListNode(6)
# l1_7 = ListNode(7)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
# l1_4.next = l1_5
# l1_5.next = l1_6
# l1_6.next = l1_7

solution = Solution()
result = solution.swapPairs(l1_1)
# print(result)
printAll(result)
