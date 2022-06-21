class Solution:
    def check(x):
        if x < -(2**31) or x > (2**31-1):
            return 0
        else:
            return 1
    def reverse(self, x: int) -> int:
        if Solution.check(x)==0:
            return 0
        if x == 0:
            return x
        
        sign = 1
        if x < 0:
            sign = -1
            x = x*sign
        x = int(str(x)[-1::-1].lstrip('0'))
        if Solution.check(x)==0:
                return 0
        else:
            return sign*x

