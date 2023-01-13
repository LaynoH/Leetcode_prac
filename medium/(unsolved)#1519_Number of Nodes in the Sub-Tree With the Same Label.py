class Solution:
    def dfs(self, tree, node, root, label, count, sub):
        itself = count[label[node]]
        count[label[node]] += 1

        for i in tree[node]:
            if i != root:
                sub = self.dfs(tree, i, node, label, count, sub)
        sub[node] = count[label[node]]-itself

        return sub

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # build the tree
        T, count = defaultdict(list), defaultdict(int)
        for ai, bi in edges:
            T[ai].append(bi)
            T[bi].append(ai)
        
        sub = [0]*n

        sub = self.dfs(T, 0, -1, labels, count, sub)
        return sub

# ref: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/3037908/python-3-11-lines-recursion-w-explanation-t-m-100-95/

