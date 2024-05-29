class Solution:
    def numSteps(self, s: str) -> int:           
        ops = 0
        while s != '1':
            if s[-1] == '0': #even, divide by 2
                s = s[:-1]
            else:
                # add 1 to s
                carry = '1'
                for idx in range(len(s) - 1, -1, -1):
                    if s[idx] == '0':
                        if carry == '1':
                            s = s[:idx] + '1' + s[idx + 1:]
                            carry = '0'
                    else:
                        if carry == '1':
                            s = s[:idx] + '0' + s[idx + 1:]
                if carry == '1':
                    s = '1' + s
            ops += 1
        return ops