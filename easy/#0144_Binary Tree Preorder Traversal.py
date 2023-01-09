# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travel(self, root, treeL):
        if not root:
            return treeL
        treeL.append(root.val)
        self.travel(root.left, treeL)
        self.travel(root.right, treeL)

        return treeL

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        treeL = []
        self.travel(root, treeL)

        return treeL
