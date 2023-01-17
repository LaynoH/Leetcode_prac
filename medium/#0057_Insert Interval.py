class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # intervals = [a,b], newInterval = [c,d]
        # c<d<a<b a<b<c<d a<c<b<d c<a<d<b c<a<b<d a<c<d<b
        for i,j in intervals:
            if j < newInterval[0]:
                res.append([i,j])
            elif newInterval[1] < i:
                res.append(newInterval)
                newInterval = [i,j]
            elif i <= newInterval[1] or j >= newInterval[0]:
                newInterval = [min(i, newInterval[0]), max(j, newInterval[1])]
        
        res.append(newInterval)
        return res
      
# ref: https://leetcode.com/problems/insert-interval/solutions/3056665/leetcode-the-hard-way-explained-line-by-line/
