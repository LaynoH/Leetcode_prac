# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root is None:
            return 0

        if root.val >= low and root.val <= high:
            sum += root.val
        else:
            sum += 0
            
        sum = sum + self.rangeSumBST(root.left, low, high)      
        sum = sum + self.rangeSumBST(root.right, low, high)

        return sum

