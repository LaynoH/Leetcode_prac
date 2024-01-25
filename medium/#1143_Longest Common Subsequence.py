class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = " " + text1
        text2 = " " + text2

        common = [[0 for j in range(len(text2))] for i in range(len(text1))]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    common[i][j] = common[i-1][j-1] + 1
                else:
                    common[i][j] = max(common[i-1][j], common[i][j-1])
        return common[-1][-1]

# ref: https://leetcode.com/problems/longest-common-subsequence/solutions/4625263/beats-96-34-users-easy-understood-solution-with-space-n-and-time-o-m-n-2-approaches
