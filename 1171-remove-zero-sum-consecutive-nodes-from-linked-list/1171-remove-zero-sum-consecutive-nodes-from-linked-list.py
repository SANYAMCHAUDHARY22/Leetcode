class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefixSumToNode = {}
        prefixSum = 0
        current = dummy
        while current:
            prefixSum += current.val
            if prefixSum in prefixSumToNode:
                prev = prefixSumToNode[prefixSum]
                toRemove = prev.next
                p = prefixSum + (toRemove.val if toRemove else 0)
                while p != prefixSum:
                    del prefixSumToNode[p]
                    toRemove = toRemove.next
                    p += toRemove.val if toRemove else 0
                prev.next = current.next
            else:
                prefixSumToNode[prefixSum] = current
            current = current.next
        return dummy.next