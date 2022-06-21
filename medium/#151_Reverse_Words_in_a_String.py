class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in s.split():
            res.append(i)
            
        str = " "
        res.reverse()
        res = str.join(res) #
        return res
      
      # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
