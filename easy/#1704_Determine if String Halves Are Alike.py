class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sLi = list(s)
        l = len(sLi)//2
        half1 = sLi[:l]
        half2 = sLi[l:]

        def checkV(li):
            v = 0
            vowels = set('aeiouAEIOU')
            for i in li:
                if i in vowels:
                    v += 1
            return v

        return checkV(half1) == checkV(half2)
