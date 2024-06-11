class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            while i in arr1:
                arr1.remove(i)
                ans.append(i)

        ans+=sorted(arr1)
        return ans