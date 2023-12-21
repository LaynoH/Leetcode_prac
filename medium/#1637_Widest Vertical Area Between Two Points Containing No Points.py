class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        axis_x = sorted(list(zip(*points))[0])
        max_w = 0

        for i in range(len(axis_x)-1):
            max_w = max(max_w, axis_x[i+1]-axis_x[i])

        return max_w

# ref: https://www.youtube.com/watch?v=q628cVxEFvU
