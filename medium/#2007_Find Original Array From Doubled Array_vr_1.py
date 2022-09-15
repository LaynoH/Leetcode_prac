class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed_len = len(changed)
        changed.sort()
        while changed:
            tmp = changed.pop(0)
            if tmp*2 in changed:   
                original.append(tmp)
                changed.pop(changed.index(tmp*2))
                continue
        if len(original)!= changed_len/2:
            original.clear()
        return original
                
                
                
