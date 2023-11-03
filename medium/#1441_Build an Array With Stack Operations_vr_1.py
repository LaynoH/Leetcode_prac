class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        res = []
        for i in range(1,n+1):
            s.append(i)
            res.append("Push")
            if s and (i not in target):
                s.pop()
                res.append("Pop")
            if s == target:
                break
        return res
