import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficultyProfit = list(zip(difficulty, profit))
        difficultyProfit.sort()

        difficulty, profit = zip(*difficultyProfit)

        n = len(profit)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(profit[i], dp[i - 1])

        result = 0
        for w in worker:
            index = bisect.bisect_right(difficulty, w) - 1
            if index < 0:
                continue
            
            result += dp[index]
        
        return result
