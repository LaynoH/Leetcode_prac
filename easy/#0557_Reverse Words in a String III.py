class Solution:
    def reverseWords(self, s: str) -> str:
        wordli = list(s.split(" "))
        res = ""
        for i in range(len(wordli)):
            wordli[i] = wordli[i][::-1]
        
        res = " ".join(wordli)
        return res
