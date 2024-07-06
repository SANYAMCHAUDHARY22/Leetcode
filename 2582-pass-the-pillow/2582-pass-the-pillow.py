class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        n-= 1                       #  <-- 1)
 
        time%= n+n                  #  <-- 2) 
        
        return n+1 - abs(n - time)  #  <-- 3