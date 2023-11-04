class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_time = 0
        right_time = 0
        for i in left:
            left_time = max(left_time, abs(0-i))

        for i in right:
            right_time = max(right_time, abs(n-i))

        return max(left_time, right_time)
