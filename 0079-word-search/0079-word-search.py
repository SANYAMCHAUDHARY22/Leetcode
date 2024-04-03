class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c,idx):
        # if idx == len(word), then word has been found
            if idx == len(word):
                return True

        # out of bounds
        # OR current letter does not match letter on board
        # OR letter already visited
            if ( 
                r<0 or r>=ROWS 
                or c<0 or c>=COLS
                or word[idx] != board[r][c]
                or (r,c) in visited
            ):
                return False
  
        # to keep track of the letter already visited, add it's position to the set
        # after DFS we can remove it from the set.
            visited.add((r,c))

        # performing DFS 
            res = (
                dfs(r+1,c,idx+1) 
                or dfs(r-1,c,idx+1) 
                or dfs(r,c+1,idx+1) 
                or dfs(r,c-1,idx+1)
            )
        
            visited.remove((r,c))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
