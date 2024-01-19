from itertools import product
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i, j in product(range(1, len(matrix)), range(len(matrix[0]))):
            matrix[i][j] += min(matrix[i-1][max(j-1, 0)], 
                                matrix[i-1][j],
                                matrix[i-1][min(j+1, len(matrix[0])-1)])
        return min(matrix[-1])

# from: https://leetcode.com/problems/minimum-falling-path-sum/solutions/4589858/only-3-lines
