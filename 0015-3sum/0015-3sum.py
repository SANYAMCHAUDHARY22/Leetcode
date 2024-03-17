class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for n,i in enumerate(nums):
            j,k=n+1,len(nums)-1
            if n>0 and i==nums[n-1]: 
                continue
            while j<k:
                sum=i+nums[j]+nums[k]
                if sum==0:
                    res.append([i,nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif sum<0:  
                    j+=1
                else:
                    k-=1
        return res