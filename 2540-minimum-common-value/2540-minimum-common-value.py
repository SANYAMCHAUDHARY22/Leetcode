class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        mp=defaultdict(int)
        for i in nums1:
            mp[i]=1
        for i in nums2:
            if mp[i]==1:
                return i
        return -1 