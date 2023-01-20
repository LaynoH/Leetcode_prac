class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freqTable = defaultdict(int)
        freqTable[0] = 1
        
        out = prefSum = 0

        for i in nums:
            prefSum += i
            remainder = prefSum % k
            # counting how many previous prefixSum have the same remainder
            out += freqTable[remainder]
            freqTable[remainder] += 1
        return out

# O(n)
# ref: https://leetcode.com/problems/subarray-sums-divisible-by-k/solutions/3070481/python3-prefix-sum-frequency-table-explained/
