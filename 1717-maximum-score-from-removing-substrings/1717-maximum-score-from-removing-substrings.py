class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_max(s,first,secand,x):
            stack = []
            point = 0
            for char in s:
                if stack and stack[-1] == first and char == secand:
                    stack.pop()
                    point += x
                else:
                    stack.append(char)
            
            return ''.join(stack), point
        
        if x>y:
            s , point = remove_and_max(s,'a','b',x)
            s , remaing_point = remove_and_max(s,'b','a',y)
            point += remaing_point
        else:
            s , point = remove_and_max(s,'b','a',y)
            s , remaing_point = remove_and_max(s,'a','b',x)
            point += remaing_point

        return point