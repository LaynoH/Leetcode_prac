class Solution:
    def dfs(self,curr,m,n,stepX,stepY):
        if stepX>=m or stepY>=n or stepX<0 or stepY<0 or curr[stepX][stepY]==0:
            return 0
        
        tmpCurr = curr[stepX][stepY]
        curr[stepX][stepY] = 0
        
        maxieUp = self.dfs(curr, m, n, stepX-1, stepY)
        maxieDown = self.dfs(curr, m, n, stepX+1, stepY)
        maxieRight = self.dfs(curr, m, n, stepX, stepY+1)
        maxieLeft = self.dfs(curr, m, n, stepX, stepY-1)

        curr[stepX][stepY] = tmpCurr
        return curr[stepX][stepY]+max(maxieUp, maxieDown, maxieRight, maxieLeft)

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxie = 0

        for i in range(m):
            for j in range(n):
                maxie = max(maxie, self.dfs(grid, m, n, i,j))
        return maxie
