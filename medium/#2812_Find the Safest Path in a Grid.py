class Solution:
    def bfs(self, grid, path, thief, n):
        while thief:
            x, y = thief.pop(0)
            currPath = path[x][y]
            self.setPath(path, x-1, y, path[x][y], thief, n)
            self.setPath(path, x+1, y, path[x][y], thief, n)
            self.setPath(path, x, y-1, path[x][y], thief, n)
            self.setPath(path, x, y+1, path[x][y], thief, n)
    # set distance to the theif
    def setPath(self, path, x, y, currPath, thief, n):
        if 0<=x<n and 0<=y<n and path[x][y] == -1:
            path[x][y] = currPath + 1
            thief.append((x,y))

    # some new function needed!!!!!!!
    def visitPath(self, path, visited, x, y, travelPath, heapq, dist, n):
        if 0<=x<n and 0<=y<n and not visited[x][y]:
            minPath = min(dist, path[x][y])
            heapq.heappush(travelPath, (-minPath, x, y))
            visited[x][y] = True

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return 0
        
        path = [[-1] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        # find the location of thieves
        thiefQ = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    path[i][j] = 0
                    thiefQ.append((i,j))

        # use bfs to define the path to the thief
        self.bfs(grid, path, thiefQ, n)

        travelPath = [(-path[0][0], 0, 0)]
        heapq.heapify(travelPath)

        while travelPath:
            dist, x, y = heapq.heappop(travelPath)
            dist *= (-1)
            if x == n-1 and y == n-1:
                return dist
            visited[x][y] = True
            self.visitPath(path, visited, x-1, y, travelPath, heapq, dist, n)
            self.visitPath(path, visited, x+1, y, travelPath, heapq, dist, n)
            self.visitPath(path, visited, x, y-1, travelPath, heapq, dist, n)
            self.visitPath(path, visited, x, y+1, travelPath, heapq, dist, n)
        return -1
        

# ref: https://leetcode.com/problems/find-the-safest-path-in-a-grid/solutions/5158873/fastest-100-easy-to-understand-clean-concise

