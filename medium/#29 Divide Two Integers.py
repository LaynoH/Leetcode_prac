class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor!=0:
            res = int(dividend/divisor)
            if res > 0:
                return min(res, (2**31-1))
            else:
                return max(res, -(2**31))
