class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n<0 or n>10**9:
            return False
        if n==1:
            return True
        
        x=1
        while x<10**9:
            inlist = [int(i) for i in str(n)] 
            tmp = [int(i) for i in str(x)] 
            if len(inlist)==len(tmp):
                for i in tmp:
                    if i in inlist:
                        inlist.pop(inlist.index(i))
            if len(inlist)==0:
                return True
            
            x*=2
                
        return False
