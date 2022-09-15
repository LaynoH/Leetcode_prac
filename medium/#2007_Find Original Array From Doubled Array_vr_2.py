class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # odd number of elements
        if len(changed)%2!=0:
            return []
        count = collections.Counter(changed)
        
        # quotient, remainder = divmod(c[0], 2) = c[0]//2, c[0]%2
        # default the number of 0s if 0 is even amount
        quotient, remainder = count[0]//2, count[0]%2
        if remainder:
            return []
        
        original = [0]*(count[0]//2)
        
        # from smallest
        for i in sorted(count.keys()):
            # it's small and no double exist
            if count[i] > count[i*2]:
                original.clear()
                break
            
            # has double
            # it's double might be other's 1/2 so just substract some of the doubles
            count[i*2]-= count[i]
            
            
            # print the number of each value but not those w 0 amount
            original.extend([i]*count[i])

        return original
        
