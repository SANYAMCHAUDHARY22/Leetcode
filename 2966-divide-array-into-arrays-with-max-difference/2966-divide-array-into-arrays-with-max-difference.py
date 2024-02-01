class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answ=[]
        n=len(nums)
        for i in range(0,n,3):
            if k<nums[i+2]-nums[i]:
                return []
            answ.append(nums[i:i+3])
        return answ       