class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        
        one=0
        two=0
        
        ans=[]
        
        while one < len(nums1) and two < len(nums2):
            
            if nums1[one] < nums2[two]:
                one+=1
            elif nums2[two] < nums1[one]:
                two+=1
            else:
                
                ans.append(nums1[one])
                one+=1
                two+=1
        return ans