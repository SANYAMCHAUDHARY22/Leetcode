class Solution:
    def minSteps(self, targetCount: int) -> int:
        if targetCount == 1:
            return 0
        minOperations = [float('inf')] * (targetCount + 1)
        minOperations[1] = 0
        
        for currentCount in range(2, targetCount + 1):
            for factor in range(1, int(currentCount**0.5) + 1):
                if currentCount % factor == 0:
                    minOperations[currentCount] = min(minOperations[currentCount], 
                                                      minOperations[factor] + currentCount // factor)
                    if factor != currentCount // factor:
                        minOperations[currentCount] = min(minOperations[currentCount], 
                                                          minOperations[currentCount // factor] + factor)
        
        return minOperations[targetCount]
