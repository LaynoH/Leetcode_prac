class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])

        def smoother(r,c):
            res, count = 0, 0
            top = max(0, r-1)
            bot = min(row, r+2)
            left_end = max(0, c-1)
            right_end = min(col, c+2)

            for i in range(top, bot):
                for j in range(left_end, right_end):
                    res += img[i][j]
                    count += 1
            return res // count

        return [[smoother(r,c) for c in range(col)] for r in range(row)]

# ref: https://www.youtube.com/watch?v=eCHajvYReSg
