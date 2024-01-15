class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(int)
        
        for i,j in matches:
            counter[i] += 0
            counter[j] -= 1
                
        win = sorted([i for i, j in counter.items() if j == 0])
        lose = sorted([i for i, j in counter.items() if j == -1])

        return [win, lose]

# ref: https://leetcode.com/problems/find-players-with-zero-or-one-losses/solutions/4567108/c-python-array-vs-hash-table-vs-bitset-262-ms-beats-100
