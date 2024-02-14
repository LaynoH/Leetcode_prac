class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, res = [],[],[]

        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
                
        for i in range(len(nums)):
            if i%2 == 0:
                tmp = pos.pop(0)
                res.append(tmp)
            else:
                tmp = neg.pop(0)
                res.append(tmp)
        return (res)

