from collections import Counter, OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = OrderedDict(freq.most_common())
        reorder = ''.join([key * value for key, value in freq.items()])

        return reorder
