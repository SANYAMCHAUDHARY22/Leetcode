class Solution(object):
    def isPowerOfTwo(self, n):
        # If n <= 0 that means its a negative hence not a power of 2...
        if n <= 0:
            return False
        if n == 1:
            return True
        # Keep dividing the number by ‘2’ until it is not divisible by ‘2’ anymore.
        while (n % 2 == 0):
            n /= 2
        # If n is equal to 1, The integer is a power of two otherwise false...
        return n == 1