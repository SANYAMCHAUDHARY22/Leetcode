class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1,c2,n=0,0,len(s)
        t=set('aieouAEIOU')
        for i in range(n//2):
            if s[i] in t: 
                c1+=1
            if s[-i-1] in t:
                c2+=1
        return True if c1==c2 else False