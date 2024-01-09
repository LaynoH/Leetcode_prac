# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(node, leaf):
            if not node:
                return
            if node and not node.left and not node.right:
                leaf.append(node.val)
            getLeaf(node.left, leaf)
            getLeaf(node.right, leaf)    

        leaf1 = []
        leaf2 = []
        getLeaf(root1, leaf1)
        getLeaf(root2, leaf2)

        return leaf1 == leaf2
