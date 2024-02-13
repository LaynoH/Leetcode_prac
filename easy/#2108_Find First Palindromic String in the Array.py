class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        tmpR = ""

        for i in words:
            tmpR = i[::-1]
            if i == tmpR:
                return i
        return ""
