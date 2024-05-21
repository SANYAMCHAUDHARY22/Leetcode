class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def solve(idx,lst):
            if idx>=n:
                ans.append(lst)
                return 
            solve(idx+1,lst)                    #Not Take
            solve(idx+1,lst+[nums[idx]])        #Take
        solve(0,[])
        return ans