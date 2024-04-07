class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize two stacks to keep track of indices of left parentheses and asterisks
        left_paren_stack, asterisk_stack = [], []
        
        # Iterate through each character in the string
        for i in range(len(s)):
            if s[i] == '(':
                # Add the index of the left parenthesis to the left_paren_stack
                left_paren_stack.append(i)
            elif s[i] == '*':
                # Add the index of the asterisk to the asterisk_stack
                asterisk_stack.append(i)
            else: # s[i] == ')'
                # If there is a left parenthesis in the left_paren_stack, pop it
                if left_paren_stack:
                    left_paren_stack.pop()
                # Otherwise, if there is an asterisk in the asterisk_stack, pop it
                elif asterisk_stack:
                    asterisk_stack.pop()
                # If there is neither a left parenthesis nor an asterisk to match the right parenthesis, the string is invalid
                else:
                    return False
        
        # Iterate through the remaining elements in the left_paren_stack and asterisk_stack
        while left_paren_stack and asterisk_stack:
            # If the index of the left parenthesis is greater than the index of the asterisk, the string is invalid
            if left_paren_stack[-1] > asterisk_stack[-1]:
                return False
            left_paren_stack.pop()
            asterisk_stack.pop()
            
        # If there are no more left parentheses to match the asterisks, the string is valid
        return not left_paren_stack