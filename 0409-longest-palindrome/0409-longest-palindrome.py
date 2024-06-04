class Solution:
    def longestPalindrome(self, s: str) -> int:
        t = set()
        for i in s:
            if i in t:
                t.remove(i)
            else:
                t.add(i)
        
        if len(t) == 0:
            return len(s)
        else:
            return len(s)-len(t) + 1