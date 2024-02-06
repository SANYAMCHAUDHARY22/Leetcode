class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        while nums:
            a=min(nums)
            alice=nums.remove(a)
            b=min(nums)
            bob=nums.remove(b)
            arr.append(b)
            arr.append(a)
        return arr
        