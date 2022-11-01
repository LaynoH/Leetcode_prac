class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2 + 1
        while low < high:
            mid = low + (high-low+1) // 2
            if mid*mid==x or (mid*mid<x and (mid+1)*(mid+1)>x):
                return mid
            elif mid * mid > x:
                high = mid-1
            else:
                low = mid
        
        return low

      # binary search
