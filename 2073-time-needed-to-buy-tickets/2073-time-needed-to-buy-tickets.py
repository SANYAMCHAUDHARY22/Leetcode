class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i,n = 0, len(tickets)
        while True:
            if i >= n:
                i = 0

            if tickets[k] == 0:
                break

            if tickets[i] != 0:
                res += 1
                tickets[i] -= 1
            
            i += 1
                
        return res