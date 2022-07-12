class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = list(s.split(" "))
        while '' in slist:
            slist.remove('')
        return len(slist[-1])
