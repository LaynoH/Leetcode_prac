class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxL = [0]
        tmpN = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i]>tmpN[-1] and nums[i]>nums[i-1]:
                maxL[-1] += 1
            elif nums[i]<tmpN[-1]:
                tmpN.append(nums[i])
                maxL.append(0)
            else:
                continue

        return max(maxL)+1
