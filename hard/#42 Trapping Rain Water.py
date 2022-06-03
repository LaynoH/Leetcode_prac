class Solution:
    def trap(self, height: List[int]) -> int:
        leftptr, rightptr = 0, len(height)-1
        leftmax, rightmax = 0, 0
        trap = 0
        
        while leftptr < rightptr:
            if height[leftptr] <= height[rightptr]:
                if height[leftptr]>leftmax:
                    leftmax = height[leftptr]
                else:
                    tmp = leftmax-height[leftptr]
                    trap += tmp
                leftptr += 1
            else:
                if height[rightptr]>rightmax:
                    rightmax = height[rightptr]
                else:
                    tmp = rightmax-height[rightptr]
                    trap += tmp
                rightptr -= 1
        return trap
        
        # https://leetcode.com/problems/trapping-rain-water/discuss/2105614/Python-Simple-O(n)-Solution-using-Two-Pointers
            
