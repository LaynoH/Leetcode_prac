class Solution:
    def maxLength(self, arr: List[str]) -> int:
        s = [""]
        maxie = 0

        for i in arr:
            if len(set(i)) != len(i):
                continue
            for j in s:
                if len(set(i+j)) != len(i+j):
                    continue
                s.append(i+j)

        for i in s:
            maxie = max(maxie, len(i))

        return maxie

# ref: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solutions/4612145/basic-python-solution-for-beginners-using-set
