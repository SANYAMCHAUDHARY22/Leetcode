class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums = list(accumulate(sorted(nums)))

        for i in range(len(nums)-1,1,-1):
            if nums[i] < 2*nums[i-1]: return nums[i]

        return -1 