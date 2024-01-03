class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev = 0

        for i in bank:
            tmp = i.count('1')
            if tmp == 0:
                continue
            beams += prev * tmp
            prev = tmp
        
        return beams
