class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def find_cuts(rectangles, axis):
            gaps = 0
            rectangles = sorted(rectangles, key = lambda seg: seg[axis])
            furthest = rectangles[0][axis+2]
            rect = rectangles[1:]

            for tmprec in rect:
                if furthest <= tmprec[axis]:
                    gaps += 1
                furthest = max(furthest, tmprec[axis+2])
            return gaps >= 2
            
        return find_cuts(rectangles, 0) or find_cuts(rectangles, 1)

     #ref https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/solutions/6533381/check-if-grid-can-be-cut-into-sections
