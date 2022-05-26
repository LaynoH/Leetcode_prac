class Solution:
    def check(x):
        if x < -(2**31) or x > (2**31-1):
            return 0
        else:
            return 1
    def reverse(self, x: int) -> int:
        if Solution.check(x)==0:
            return 0
        if x ==0:
            return x
        if x < 0:
            strX = '-'+str(x)[-1:0:-1]
            x = int(strX.lstrip('0'))           #newly learned: .lstrip()
            if Solution.check(x)==0:
                return 0
            return x
        else:
            x = int(str(x)[-1::-1].lstrip('0'))
            if Solution.check(x)==0:
                return 0
            return x
