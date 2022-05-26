class Solution:    
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        if len(s)==0:
            return len(s)
        elif s.isspace() or len(s)==1:
            return 1
        elif len(s)==2:
            if s[0]!=s[1]:
                return 2
            else:
                return 1
        else:
            for i in range(len(s),1,-1):
                sub = []
                for j in range(0,len(s)-i+1):   # run max-i times
                    sub = s[j:j+i]
                    repeat = 0
                    for k in range(len(sub)):
                        if sub[k] in sub and sub.index(sub[k])!=k:
                            repeat = 1
                    if repeat == 0:
                        count = len(sub)
                        return count
        return 1
