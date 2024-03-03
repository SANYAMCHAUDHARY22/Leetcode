# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        count=0
        curr=head
        while curr:
           count+=1
           curr=curr.next
        check=count-n-1
        count=0
        curr=head
        if check==-1:
            return head.next
        while curr:
            if count==check:
                curr.next=curr.next.next
                break
            curr=curr.next
            count+=1
        return head