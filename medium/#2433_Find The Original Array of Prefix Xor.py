class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        tmp = pref[0]
        for i in range(1, len(pref)):
            pref[i] = tmp ^ pref[i]
            tmp = tmp ^ pref[i]
            #pref[i] ^= tmp
            #tmp ^= pref[i]
        return pref
