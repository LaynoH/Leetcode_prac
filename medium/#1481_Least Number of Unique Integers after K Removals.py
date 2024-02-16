from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).items(),key = lambda i: i[1])
        freqli = []

        for i in freq:
            freqli.extend([i[0]]*i[1])
        
        return len(set(freqli[k:]))
