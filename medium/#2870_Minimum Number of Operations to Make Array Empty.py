class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oper = 0
        freq = [0] * (max(nums) + 1)

        for i in nums:
            freq[i] += 1

        for i in freq:
            if oper == -1:
                break
            while i > 0:
                if i>=3 and (i-2) !=2 :
                    i-=3
                    oper += 1
                    
                elif i>=2:
                    i-=2
                    oper += 1
                else:
                    oper = -1
                    break
        return oper
