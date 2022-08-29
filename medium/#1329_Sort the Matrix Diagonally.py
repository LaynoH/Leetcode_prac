class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        # row+col-2 = number of diagonal line
        for i in range(1, row+col-2):   
            # find start point
            if i<row:
                tmpR, tmpC = row-i-1, 0
            else:
                tmpR, tmpC = 0, i-row+1
                
            diagonal = []
            
            # store in a list
            while tmpR<row and tmpC<col:
                diagonal.append(mat[tmpR][tmpC])
                tmpR, tmpC = tmpR+1, tmpC+1
                
            # sort the numbers in list
            diagonal.sort()
            
            tmpR, tmpC = tmpR-1, tmpC-1
            
            # put back in matrix
            while tmpR>=0 and tmpC>=0:
                mat[tmpR][tmpC] = diagonal.pop()
                tmpR, tmpC = tmpR-1, tmpC-1
                
        return mat
                
