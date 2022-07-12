class Solution:
    def reverseWords(self, s: str) -> str:
        res = list(s.split(" "))
        while '' in res:
            res.remove('')
        
        str = " "
        res.reverse()
        res = str.join(res) #
        return res
    
        
