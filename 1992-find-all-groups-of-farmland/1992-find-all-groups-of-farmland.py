class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        m, n, ans = len(land), len(land[0]), []
        land = [[0]*(n+1)]+[[0]+row for row in land]  

        for r in range(1,m+1):                                              
            for c in range(1,n+1):                                         

                if land[r][c] and not land[r-1][c] and not land[r][c-1]:   

                    R, C = r, c
  
                    while R < m and land[R+1][c]: R+= 1                     
                    while C < n and land[r][C+1]: C+= 1                                 
                    ans.append([r-1,c-1,R-1,C-1])                           

        return  ans