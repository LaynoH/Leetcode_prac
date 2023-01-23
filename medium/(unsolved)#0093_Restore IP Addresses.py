class Solution:
    def backtrace(self, s, addr, i, out):
        if i == len(s): 
            if len(addr) == 4:
                out.append('.'.join(map(str,addr)))
            return out
        if addr[-1]!=0 and addr[-1]*10+int(s[i]) <= 255:
            last = addr[-1]
            addr[-1] = addr[-1]*10 + int(s[i])
            self.backtrace(s, addr, i+1, out)
            addr[-1] = last
        
        if len(addr)<4:
            self.backtrace(s, addr+[int(s[i])], i+1, out)
        
        return out

    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        out = self.backtrace(s, [int(s[0])], 1, out)
        return out
    
# ref: https://leetcode.com/problems/restore-ip-addresses/solutions/3079133/python3-backtracking-for-beginners/
