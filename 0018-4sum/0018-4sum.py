class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.findNSum(nums, target, 4, [], res)
        return res

    def findNSum(self, nums, target, N, prefix, result):
        L = len(nums)
        if N == 2:
            l, r = 0, L-1
            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    result.append(prefix + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1
                elif add > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(L-N+1):
                if target < N*nums[i] or target > N*nums[-1]: # key judgement
                    break
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    self.findNSum(nums[i+1:], target-nums[i], N-1, prefix+[nums[i]], result)
        return