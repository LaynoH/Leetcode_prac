class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmpr = str(x)[-1::-1]
        tmpx = str(x)
        if(tmpx==tmpr) or len(tmpx)==1:              
            return True
        else:
            return False
