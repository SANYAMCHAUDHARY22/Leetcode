from collections import defaultdict
class Solution:
    def atmostk(self,n,k,nums):
        l=0
        r=0
        map=defaultdict(int)
        ans=0
        while r<n:
            map[nums[r]]+=1
            while len(map)>k:
                map[nums[l]]-=1
                if map[nums[l]]==0:
                    del map[nums[l]]
                l+=1
            
            ans+=r-l+1
            r+=1
        return ans
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostk(len(nums),k,nums)-self.atmostk(len(nums),k-1,nums)