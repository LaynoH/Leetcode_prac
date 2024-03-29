# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        queue = deque([root])
        depth = 1
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not (node.left or node.right):
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
# ref: https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/2158815/Python-BFS-solution
# ref: https://www.tutorialspoint.com/python/python_deque.htm
            
