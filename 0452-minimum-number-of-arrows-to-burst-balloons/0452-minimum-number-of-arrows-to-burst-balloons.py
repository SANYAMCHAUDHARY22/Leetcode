class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pts = sorted(points, key=lambda el: el[1])
        
        res, combo = 0, (float("-inf"), float("-inf"))
        for start, end in pts:
            if start <= combo[1]: # overlaps?
                combo = (max(combo[0], start), min(combo[1], end))
            else:
                combo = (start, end)
                res += 1
                
        return res