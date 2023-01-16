class Solution:
    def getOri(self,x,ori):
        if x == ori[x]:
            return x
        else:
            ori[x] = self.getOri(ori[x],ori)
            return ori[x]
            #return self.getOri(ori[x],ori)

    def unite(self, tree, vals, path):
        ori, countP = list(range(path)), [1]*path
        for i, j in tree:
            ai, bi = self.getOri(i,ori), self.getOri(j,ori)

            if vals[ai] == vals[bi]:
                path += countP[ai]*countP[bi]
                ori[ai] = bi
                countP[bi] += countP[ai]
            elif vals[ai] < vals[bi]:
                ori[ai] = bi
            else:
                ori[bi] = ai
            
        return path

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        path = len(vals)
        if path <= 1:
            return path
        tree = edges
        tree.sort(key = lambda validx: max(vals[validx[0]], vals[validx[1]]))
        path =  self.unite(tree, vals, path)   
        return path

# ref: https://leetcode.com/problems/number-of-good-paths/solutions/3053175/leetcode-the-hard-way-explained-line-by-line/
