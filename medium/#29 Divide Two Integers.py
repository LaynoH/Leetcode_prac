class Solution:
    def check(x):
        if x < -(2**31) or x > (2**31-1):
            return 0
        else:
            return 1
    def divide(self, dividend: int, divisor: int) -> int:
        if Solution.check(dividend) == 0:
            return dividend
        if divisor!=0:
            res = int(dividend/divisor)
            if Solution.check(res) == 0:
                if res > 0:
                    return (2**31-1)
                else:
                    return -(2**31)
            return res
