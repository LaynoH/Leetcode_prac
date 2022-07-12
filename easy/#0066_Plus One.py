class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        index = 0
        while carry==1:
            if index==len(digits):
                digits.append(1)
                carry=0
            elif digits[index]+1>9:
                digits[index]=0
                index+=1
                carry=1
            else:
                digits[index] += 1
                carry=0
        digits.reverse()
        return digits
        
        
        
