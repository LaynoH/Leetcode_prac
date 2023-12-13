class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #s = ''.join(sorted(s))
        #t = ''.join(sorted(t))
        #while t and s:
        #    ttmp = t[0]
        #    t = t[1:]
        #    stmp = s[0]
        #    s = s[1:]
        #    if ttmp != stmp:
        #        return ttmp
        #return t[0] 
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        while t and s:
            ttmp = t.pop(0)
            stmp = s.pop(0)
            if ttmp!=stmp:
                return ttmp
        return t.pop(0)
