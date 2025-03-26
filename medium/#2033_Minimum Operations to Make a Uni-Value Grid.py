class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatten_g = []
        result = 0

        for row in grid:
            for i in row:
                flatten_g.append(i)
        
        flatten_g.sort()
        length = len(flatten_g)
        common_num = flatten_g[length // 2]

        for i in flatten_g:
            if i % x != common_num % x:
                return -1
            result += abs(common_num - i) // x
        
        return result
    # ref https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/solutions/6525276/minimum-operations-to-make-a-uni-value-grid
