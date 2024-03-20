# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pos, a_node = 0, list1
        while pos < a - 1:          # let a_node point to the list1 node at index a - 1
            a_node = a_node.next
            pos += 1
        b_node = a_node
        while pos < b + 1:          # let b_node point to the list1 node at index b + 1
            b_node = b_node.next
            pos += 1
        a_node.next = list2         # put list2 after a_node
        while list2.next:
            list2 = list2.next
        list2.next = b_node         # put list2 before b_node
        return list1 
        