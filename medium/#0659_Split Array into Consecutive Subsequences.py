import collections
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        sub = collections.defaultdict(int)
#       elements = list(dict.fromkeys(nums))
#       freq = dict(zip(elements,[nums.count(i) for i in elements]))
        freq = collections.Counter(nums)

        for i in nums:
#           does not have it in nums
            if freq[i] == 0:
                continue
            
            freq[i] -= 1
#           1. able to add to exist subsequence
#           any subsequence end with [num-1]?
#           yes -> add to the subsequence and make it ends with i
#           (so subsequence end with i-1 will be one less)
            if sub[i-1]>0:
                sub[i-1] -= 1
                sub[i] += 1

#           2. create a new subsequence
#           make sure they have two more elements following to make subsequence len = 3
            elif freq[i+1] and freq[i+2]:
                freq[i+1] -= 1
                freq[i+2] -= 1
                sub[i+2] += 1
#           3. unable to start new subsequence/fit in subsequence
            else:
                return False
                
        return True
      
# ref: https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/2448243/Python-oror-Easily-Understood-oror-Faster-than-90-oror-Explanation
# ref: https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/2446738/Python-524ms-98.3-Faster-Multiple-solutions-94-memory-efficient
