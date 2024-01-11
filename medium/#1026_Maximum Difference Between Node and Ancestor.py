# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def preorder(node, minie, maxie):
            if not node:
                return abs(minie - maxie)
            
            minie = min(minie, node.val)
            maxie = max(maxie, node.val)

            lchild = preorder(node.left, minie, maxie)
            rchild = preorder(node.right, minie, maxie)

            return max(lchild, rchild)
            
        return preorder(root, root.val, root.val)

# ref: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/solutions/4543610/beats-100-brute-optimal-both-explained-java-c-python
