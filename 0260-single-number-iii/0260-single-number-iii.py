class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        dc=defaultdict(lambda:0)
        for a in(nums):
            dc[a]+=1
        ans=[]
        for a in dc:
            if(dc[a]==1):
                ans.append(a)
        return ans