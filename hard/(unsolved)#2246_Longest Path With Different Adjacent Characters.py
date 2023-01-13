class Solution:
    def dfs(self, tree, node, path, s):
        long1, long2 = 0,0
        for i in tree[node]:
            pathSub, path = self.dfs(tree,i,path,s)
            if s[i] != s[node]:
                # algo for 2 longest path on each side of current node
                if pathSub > long1:
                    long2,long1 = long1,pathSub
                elif pathSub > long2:
                    long2 = pathSub

        # long1+long2+1 = the longest path pass through current node 
        path = max(path, long1+long2+1)
        return long1+1, path
    
    def longestPath(self, parent: List[int], s: str) -> int:
        T = defaultdict(list)

        # enumerate(parent) ex.
        #   [(0,-1), (1,0), (2,0), (3,1), (4,1), (5,2)]
        #   exactly like the dict we need
        #   but we want to store in inversely in ()
        #   [(-1,0), (0,1), (0,2), (1,3), (1,4), (2,5)]
        for ai, bi in enumerate(parent):
            T[bi].append(ai)
        
        tmp,path = self.dfs(T,0,1,s)
        return path

# ref: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/3042992/python3-dfs-explained/

