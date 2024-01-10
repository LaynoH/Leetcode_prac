# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        maxMin = 0
        def getTime(node, start):
            if not node:
                return 0
            ltime = getTime(node.left, start)
            rtime = getTime(node.right, start)

            if node.val == start:
                Solution.maxMin = max(ltime, rtime)
                return -1
            elif ltime>=0 and rtime>=0:
                return max(ltime, rtime) + 1
            
            Solution.maxMin = max(Solution.maxMin, abs(ltime-rtime))
            return min(ltime, rtime) - 1

        getTime(root, start)
        return Solution.maxMin

# ref: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/solutions/4538708/o-n-java-python-javascript-typescript-c-c-binary-tree
