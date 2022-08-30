class Solution:
    def transpose(self, matrix):
        for r in range(len(matrix)):
            for c in range(r+1,len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix
    
    
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        self.transpose(matrix)
        for i in range(row):
            matrix[i].reverse()
        
# matrix rotation:
# 1. transpose -> reverse column
# 2. reverse row -> transpose
