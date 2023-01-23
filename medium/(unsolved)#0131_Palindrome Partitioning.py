class Solution:
    def valid(self,s,start,end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1
        return True

    def palindromesub(self,s,idx,output,tmp):
        if idx == len(s):
            return output.append(tmp[:])
        for i in range(idx, len(s)):
            if self.valid(s, idx, i):
                tmp.append(s[idx:i+1])
                self.palindromesub(s, i+1, output, tmp)
                tmp.pop()
        return output

    def partition(self, s: str) -> List[List[str]]:
        return self.palindromesub(s,0,[],[])
        
# ref: https://leetcode.com/problems/palindrome-partitioning/solutions/3083493/day-22-beginner-friendly-solution-with-diagram-backtracking/
