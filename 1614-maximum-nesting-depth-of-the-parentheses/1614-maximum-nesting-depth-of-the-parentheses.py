class Solution:
    def maxDepth(self, s: str) -> int:
        depths = [0]
        
        count = 0
        for i in s:
            if(i == '('):
                count += 1
            elif(i == ')'):
                count -= 1
            depths.append(count)
        
        return max(depths)