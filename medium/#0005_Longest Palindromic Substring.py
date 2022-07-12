class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        
        def findPali(s, left, right):
            while(right<len(s) and left>=0 and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        
        
        for i in range(len(s)):
            #(original, odd, even)
            res = max(res, findPali(s,i,i), findPali(s,i,i+1) ,key=len)
                
        return res
        
