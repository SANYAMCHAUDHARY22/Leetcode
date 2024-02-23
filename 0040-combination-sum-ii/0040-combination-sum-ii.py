class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        list1=[]
        candidates.sort()
        def dfs(candidates,target,path,list1):
            if target==0:
                list1.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                if i>=1 and candidates[i]==candidates[i-1]:
                    continue
                dfs(candidates[i+1:],target-candidates[i],path+[candidates[i]],list1)
        dfs(candidates,target,[],list1)
        return list1