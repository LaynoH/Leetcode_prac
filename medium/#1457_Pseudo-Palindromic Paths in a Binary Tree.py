# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(node, freq):
        if not node:
            return 0
        freq[node.val] ^= 1
        res = ((node.left == node.right and sum(freq) < 2)+
                Solution.dfs(node.left, freq)+
                Solution.dfs(node.right, freq))
        freq[node.val] ^= 1
        return res
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        return Solution.dfs(root, [0]*10)

# ref: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solutions/4616636/dfs-solution-only-xor-and-sum
