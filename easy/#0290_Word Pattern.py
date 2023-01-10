class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        patL = [i for i in pattern]
    
        if len(set(pattern)) != len(set(s)): return False

        diff = list(zip_longest(pattern, s))
        
#        item, comp = [], []
#        for i in diff:
#            if i not in item:
#                item.append(i)
#        for i in patL:
#            if i not in comp:
#                comp.append(i)
        
        if len(set(diff)) == len(set(pattern)): return True
        return False

# ref: https://leetcode.com/problems/word-pattern/solutions/2977027/python-3-2-lines-w-explanation-t-m-98-100/
# ref: https://leetcode.com/problems/word-pattern/solutions/2976957/simple-python-easy-10-lines-to-understand-faster-then-95/
