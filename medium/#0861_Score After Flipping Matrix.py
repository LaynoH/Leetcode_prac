class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_1 = 0

        # calculating the sum of first column (should all being 1)
        output = (1 << (n-1)) * m

        trans = list(zip(*grid))

        for i in range(1, n):
            # 2^(pos_val)
            pos_val = 1 << (n-1-i)
            # get difference between first column and others
            count_1 = len([j for j,k in zip(trans[0], trans[i]) if j^k])
            output += max(count_1, m-count_1) * pos_val  
        return output
                

# ref: https://leetcode.com/problems/score-after-flipping-matrix/solutions/5149964/fastest-100-easy-to-understand-clean-concise
# ref: https://leetcode.com/problems/score-after-flipping-matrix/solutions/5150856/think-in-terms-of-bit-positions-java-c
