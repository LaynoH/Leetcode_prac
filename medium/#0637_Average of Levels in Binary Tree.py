# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root])
        ave = []
        
        # bfs
        while queue:
            # level sum
            lvsum = 0
            # number of nodes at this level
            lvnum = len(queue)
            
            for i in range(lvnum):
                # pop the left side in the queue
                curr = queue.popleft()
                lvsum += curr.val
                
                if curr.left:
                    # append left child on right side of queue
                    queue.append(curr.left)

                if curr.right:
                    # append right child on right side of queue
                    queue.append(curr.right)
            
            ave.append(lvsum / lvnum)
            
        return ave
                    
