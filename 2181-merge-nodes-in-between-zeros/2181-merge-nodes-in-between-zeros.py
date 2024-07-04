class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # Dummy node to simplify list construction
        currentNew = dummy # Pointer to construct new list
        currentOld = head.next # Start from the node after the initial zero

        sum = 0
        
        while currentOld is not None:
            if currentOld.val == 0:
                # When we hit a zero, we need to create a new node with the sum if sum is non-zero
                if sum != 0:
                    currentNew.next = ListNode(sum)
                    currentNew = currentNew.next
                    sum = 0 # Reset sum for the next segment
            else:
                # Accumulate the sum of values between zeros
                sum += currentOld.val
            currentOld = currentOld.next

        return dummy.next # The first node in the dummy list is the start of the result list
