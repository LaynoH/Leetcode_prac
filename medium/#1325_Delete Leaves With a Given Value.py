# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, curr, target):
        if not curr:
            return

        curr.left = self.dfs(curr.left, target)
        curr.right = self.dfs(curr.right, target)
        
        if not curr.left and not curr.right and curr.val == target:
            return 

        return curr
            
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        root = self.dfs(root, target)
        return root
