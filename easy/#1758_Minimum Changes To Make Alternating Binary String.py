class Solution:
    def minOperations(self, s: str) -> int:
        alter = 0
        for i in range(len(s)):
            if int(s[i]) != i%2:
                alter += 1
        return min(alter, len(s)-alter)

        #s = list(s)
        #for i in range(1,len(s)):
        #    if s[i]==s[i-1]:
        #        alter += 1
        #        s[i] = str(abs(int(s[i])-1))
        #return min(alter, len(s)-alter)
