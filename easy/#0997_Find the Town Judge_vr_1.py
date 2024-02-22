class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        judge = -1
        for ai, bi in trust:
            trusted[ai] -=1
            trusted[bi] +=1

        for i in range(1,n+1):
            if trusted[i] == n-1:
                judge = i
                break

        return judge
