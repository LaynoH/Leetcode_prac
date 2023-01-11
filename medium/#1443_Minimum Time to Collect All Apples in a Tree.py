class Solution:
    def dfs(self, tree, node, root, apple):
        time = 0
        for i in tree[node]:
            if i != root:
                time += self.dfs(tree, i, node, apple)
        # if time: there's apple at gradnchild node or great grandchild node
        # if apple[node]: this is apple
        if time or apple[node]:
            # +2: back and forth
            return time + 2
        # nothing at this branch, return 0
        return time

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # build tree
        tree = defaultdict(list)
        for ai, bi in edges:
            tree[ai].append(bi)
            tree[bi].append(ai)
        # extra 2 added so -2 here
        # when no apple: dfs() = 0, it'll be -2 so limit w 0
        return max(self.dfs(tree, 0,-1, hasApple)-2, 0)
      
# ref: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/3033301/python3-dfs-explained/
