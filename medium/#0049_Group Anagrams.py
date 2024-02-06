class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            tmp = "".join(sorted(i))

            if tmp not in res:
                res[tmp] = [i]
            else:
                res[tmp].append(i)
        return res.values()
