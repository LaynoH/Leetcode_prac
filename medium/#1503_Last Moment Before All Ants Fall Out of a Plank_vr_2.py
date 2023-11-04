class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        move_left = max(left, default = 0)
        move_right = n-min(right, default = n)

        return max(move_left, move_right)
