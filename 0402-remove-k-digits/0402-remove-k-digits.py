class Solution:

    # O(N) O(N)
    def removeKdigits(self, nums: str, k: int) -> str:

        if len(nums)==1: # if only 1 digit we can only get 0 
            return "0"

        stack = []
        
        for num in nums:
            # k--> no of deletion
            # len(nums)-k --> len of our answer --> len of stack at last
            while stack and stack[-1]>num and k>0:
                stack.pop()
                k-=1
            stack.append(num)

        # a case like [112] k = 1    no deletion will happen because there is no valley
        # so we pop k elements from last
        while k>0 and stack:
            stack.pop()
            k-=1
 
        return ''.join(stack).lstrip("0") or "0"  # lstrip is for removal of cases where stack is  000200
		
		# but our ans should be 200