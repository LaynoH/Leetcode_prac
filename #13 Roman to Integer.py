class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            if s[i]=='I':
                if i+1<len(s) and (s[i+1]=='V' or s[i+1]=='X'):
                    out-=1
                else:
                    out+=1
            elif s[i]=='V':
                out+=5
            elif s[i]=='X':
                if i+1<len(s) and (s[i+1]=='L' or s[i+1]=='C'):
                    out-=10
                else:
                    out+=10
            elif s[i]=='L':
                out+=50
            elif s[i]=='C':
                if i+1<len(s) and (s[i+1]=='D' or s[i+1]=='M'):
                    out-=100
                else:
                    out+=100
            elif s[i]=='D':
                out+=500
            elif s[i]=='M':
                out+=1000
        return out
