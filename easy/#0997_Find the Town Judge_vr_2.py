class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            if n == 1:
                return 1
            else:
                return -1
        
        a, b = list(zip(*trust))
        a = list(a)
        b = list(b)

        for i in range(1, n+1):
            if i in b and i not in a and (b.count(i) == (n-1)):
                return i
        return -1
