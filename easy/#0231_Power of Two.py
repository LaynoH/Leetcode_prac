class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i <= n:
            if n == 2**i:
                return True
            i+=1
        return False
                
