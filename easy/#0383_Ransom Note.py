class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Rlist=[i for i in ransomNote]
        Mlist = [i for i in magazine]

        for i in Rlist:
            if i in Mlist:
                Mlist.pop(Mlist.index(i))
            else:
                return False    
        return True
