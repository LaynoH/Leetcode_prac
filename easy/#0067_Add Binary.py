class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        lia = [int(i) for i in a]
        lib = [int(i) for i in b]
        added = ''
        
        while lia or lib or carry:
            if lia:
                carry += lia.pop()
            if lib:
                carry += lib.pop()
            added = added + str(carry%2)
            
            carry = carry//2
            
        return added[::-1] 
            
