class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        ctr = Counter(nums)                                 # <-- 1.
        mx = max(ctr.values())                              # <-- 2.
        return sum(filter(lambda x: x == mx, ctr.values())) # <-- 3.