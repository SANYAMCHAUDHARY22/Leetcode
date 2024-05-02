class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        return max(({x for x in nums if -x in nums}), default=-1)