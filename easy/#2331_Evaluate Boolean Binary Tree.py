# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, curr):
        if curr.val == 0 or curr.val == 1:
            return curr.val == True
        if curr.val == 2:
            return self.postorder(curr.left) or self.postorder(curr.right)
        if curr.val == 3:
            return self.postorder(curr.left) and self.postorder(curr.right)
        return False

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.postorder(root)
