class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCounter = 0
        for num in arr:
            if num % 2 == 0:
                oddCounter = 0  
                continue
            else:
                oddCounter += 1  
            if oddCounter == 3:
                return True  
        return False  