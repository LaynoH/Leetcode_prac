# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf = []
        def getLeaf(node):
            if node == None:
                return
            if node and ndoe.left == None and node.right == None:
                leaf.append(node.val)
            getLeaf(node.left)
            getLeaf(node.right)    
            return leaf

        leaf1 = getLeaf(root1)
        leaf.clear()
        leaf2 = getLeaf(root2)

        return leaf1 == leaf2
