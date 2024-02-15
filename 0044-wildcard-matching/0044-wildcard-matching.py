class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s);
        m = len(p);
        dp = [[0]*(m+1) for _ in range(0,n+1)]

        dp[0][0] = 1
        for j in range(1,m+1):
            if(p[j-1] == '*' ): dp[0][j] = dp[0][j-1];

        for i in range(1,n+1):
            for j in range(1,m+1):
                if(s[i-1] == p[j-1] or p[j-1] == '?' ): dp[i][j] = dp[i-1][j-1]
                elif( p[j-1] == '*' ):
                    # did we match without the chracter in s or did we match with the character before '*' in p
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]