# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0
    
    # go through every nodes no matter it's good or not
    def dfs(self, current, maxpath):
        if not current:
            return
        
        # each node that has path all smaller than it +1
        if current.val>= maxpath:
            self.good+=1
        
        # in case the max node in path is bigger than current node, vice versa
        maxpath = max(current.val, maxpath)
        
        # left child node
        if current.left:
            self.dfs(current.left,maxpath)
        
        # right child node
        if current.right:
            self.dfs(current.right, maxpath)
        
        
    def goodNodes(self, root: TreeNode) -> int:
        # each node's value is between [-10^4, 10^4] so use the smallest value -1 to be our defaul value for max path
        self.dfs(root, float(-10001)) # can also use self.dfs(root, float('-inf'))
        
        
        return self.good
        
# ref https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/2549504/Simple-Python-Solution
        
