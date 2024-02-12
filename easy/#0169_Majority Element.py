class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int) 
        for i in nums: 
            d[i] += 1

        maxItem = max(d.items(), key=lambda a: a[1])

        return maxItem[0]
