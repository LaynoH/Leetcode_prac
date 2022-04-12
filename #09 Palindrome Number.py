class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            tmpr = [int(i) for i in str(x)]
            tmpr.reverse()
            tmpx = [int(i) for i in str(x)]
            if(tmpx==tmpr) or len(tmpx)==1:
                return True
            else:
                return False
        else:
            return False
