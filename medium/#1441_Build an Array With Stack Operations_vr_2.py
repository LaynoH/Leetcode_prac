class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if not target:
                break
            tmp = target.pop(0)
            res.append("Push")
            if tmp!=i:
                res.append("Pop")
                target = [tmp] + target
        return res
