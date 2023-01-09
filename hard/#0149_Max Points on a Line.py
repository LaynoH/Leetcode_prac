from collections import defaultdict
class Solution:
    def gcd(a, b):
        if a == b:
            return a
        if a > b:
            gcd(a – b, b)
        else:
            gcd(a, b – a)
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()

        # maximum number of points on a longest line
        maxS = 0

        # from the first points and 
        for i,(x1,y1) in enumerate(points):
            #############################################################
            # make dictionary of combination of slopes for each (x1,y1) #
            #############################################################
            slope = defaultdict(int)

            # see the slope of each (x1,y1) to other points
            for x2, y2 in points[i+1:]:
                # difference of x1,x2 and y1,y2
                dx, dy = x2 - x1, y2 - y1
                G = gcd(dx, dy)
                # find the slope of (x1,y1) to (y1,y2)
                tmpS = (dx//G,dy//G)

                slope[tmpS] += 1
                if slope[tmpS] > maxS: 
                    maxS = slope[tmpS]
        return maxS+1

# ref: https://leetcode.com/problems/max-points-on-a-line/solutions/3016632/python-3-11-lines-w-explanation-and-example-t-m-95-97/
