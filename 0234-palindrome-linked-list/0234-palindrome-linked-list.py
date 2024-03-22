class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]   