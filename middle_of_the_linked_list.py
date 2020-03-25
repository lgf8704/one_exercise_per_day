"""Date: 2020-3-23
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second node.

EXample 1:

Input: [1, 2, 3, 4, 5]
Output: Node 3 from this list (Serialization: [3, 4, 5])
The returned node has value 3. (The judge's serialization of this node is [3, 4, 5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next.val = NULL.

Example 2:

Input: [1, 2, 3, 4, 5, 6]
Output: Node 4 from this list (Serialization: [4, 5, 6])
Since th list has two middle nodes with value 3 and 4, we return the second one.

Notes:
    The numbers of nodes in the given list will be between 1 and 100.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def middle_node(head: ListNode) -> ListNode:
        node = head.next
        num = 1
        while node is not None:
            node = node.next
            num += 1

        node = head
        middle_num = num // 2
        while middle_num > 0:
            node = node.next
            middle_num -= 1

        return node


if __name__ == "__main__":

    # 定义3个节点
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    # 将3个节点链接在一起，头节点是node1
    node1.next = node2
    node2.next = node3

    # 调用Solution.middle_node方法
    mid_node = Solution.middle_node(node1)
    print(mid_node)
    while mid_node is not None:
        print(mid_node.val)
        mid_node = mid_node.next
