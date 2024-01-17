class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occdict = defaultdict(int)
        for i in arr:
            occdict[i] += 1
        occ = list(occdict.values())

        return len(occ) == len(set(occ))
        
