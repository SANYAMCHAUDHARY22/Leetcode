class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse = True)
        
        arr = list(enumerate(happiness[:k]))
 
        return sum(map(lambda x: max(x[1]-x[0], 0), arr))