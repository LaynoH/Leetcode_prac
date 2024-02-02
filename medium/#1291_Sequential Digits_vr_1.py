class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []

        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                tmp = int(digits[i:j+1])
                if tmp > high:
                    break
                if tmp >= low:
                    res.append(tmp)
        res.sort()
        return res

# ref: https://leetcode.com/problems/sequential-digits/solutions/4664743/video-give-me-4-minutes-how-we-think-about-a-solution-bonus-python-javascript-java-and-c
