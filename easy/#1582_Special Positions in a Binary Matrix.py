class Solution:    
    def checkCol(mat, idx):
            if sum(r[idx] for r in mat)==1:
                return 1
            return 0
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = 0
        for r in mat:
            if sum(r)==1:
                idx = r.index(1)
                special += Solution.checkCol(mat,idx)
        return special
                
# ref: https://leetcode.com/problems/special-positions-in-a-binary-matrix/solutions/4397604/video-give-me-5-minutes-how-we-think-about-a-solution/
