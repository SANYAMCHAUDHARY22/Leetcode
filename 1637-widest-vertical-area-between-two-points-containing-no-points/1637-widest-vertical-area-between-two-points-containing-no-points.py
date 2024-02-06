class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        result=0
        for i in range(len(points)-1):
            result=max(result,points[i+1][0]-points[i][0])
        return result
        
        