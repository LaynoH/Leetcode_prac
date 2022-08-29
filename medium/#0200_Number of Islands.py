class Solution:
    def dfs(self, grid, row, col):
        m, n = len(grid), len(grid[0])
        if(row<0 or col<0 or row>=m or col>=n or grid[row][col]=='0'):
            return
        
        grid[row][col]='0'
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)
            
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1'):
                    island+=1
                    self.dfs(grid, i, j)
        return island
            
            
