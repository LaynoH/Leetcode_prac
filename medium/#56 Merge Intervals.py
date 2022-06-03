class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals.pop(0)]
        for element in intervals:
            end = res[-1][1]
            if end >= element[0]:
                res[-1][1] = max(element[1], end)
            else:
                res.append(element)
        return res
      
