class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # initial
        next_byte = 0
        
        for i in data:
            # first/last byte
            if next_byte ==0:
                # 2 bytes (110xxxxx)
                if i>>5 == 0b110:
                    next_byte = 1
                # 3 bytes (1110xxxx)
                elif i>>4 == 0b1110:
                    next_byte = 2
                # 4 bytes (11110xxx)
                elif i>>3 == 0b11110:
                    next_byte = 3
                # suppose to be 1 byte but it's not 0xxxxxxx
                elif i>>7 != 0b0:
                    return False
            # not first/last byte
            else:
                # not the first/last byte but also not 10xxxxxx
                if i>>6 != 0b10:
                    return False
                next_byte-=1
                               
        if next_byte == 0:
            return True
        
        # 0b https://stackoverflow.com/questions/46002161/what-does-the-0b-mean-at-the-begining-of-the-byte-0b1100010
        # ref: https://leetcode.com/problems/utf-8-validation/discuss/2575460/Easy-Python-Solution
