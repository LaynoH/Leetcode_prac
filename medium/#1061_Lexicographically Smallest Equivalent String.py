import string
class Solution:
    # get to the origin char of x
    def getOri(self,x,ori):
        if x == ori[ord(x)-ord('a')]:
            return x
        return self.getOri(ori[ord(x)-ord('a')],ori)
    # see if it's connected to other alphabet char
    def unite(self,x,y,ori):
        x = self.getOri(x,ori)
        y = self.getOri(y,ori)
        # if smaller, replace
        if x < y:
            ori[ord(y)-ord('a')] = x
        else:
            ori[ord(x)-ord('a')] = y
        return ori
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:     
        outLi, outStr = [], ""
        # set up alphabet origin table using list
        ori = list(string.ascii_lowercase)
        # read in s1, s2 to set up origin table
        for i in range(len(s1)):
            ori = self.unite(s1[i],s2[i],ori)
        
        # replacement
        for i in baseStr:
            outLi.append(self.getOri(i,ori))
        # list to str    
        outStr = ''.join(outLi)
        return outStr

# ref: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/solutions/3047649/leetcode-the-hard-way-explained-line-by-line/
