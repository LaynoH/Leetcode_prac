class Solution:
    def isValid(self, s: str) -> bool:
        slist = list(s)
        tmp = []
        flag=0
        while slist:
            if slist[0]=='(' or slist[0]=='{' or slist[0]=='[':
                flag=1
                tmp.append(slist.pop(0))
            elif tmp and slist[0]==')' and tmp[-1]=='(' :
                slist.pop(0)
                tmp.pop()
            elif tmp and slist[0]==']' and tmp[-1]=='[' :
                slist.pop(0)
                tmp.pop()
            elif tmp and slist[0]=='}' and tmp[-1]=='{' :
                slist.pop(0)
                tmp.pop()
            elif not(tmp) and (slist[0]==')' or slist[0]==']' or slist[0]=='}'):
                return False
            else:
                slist.pop(0)
                flag=0
                
        if not (tmp) and flag==1:
            return True
        else:
            return False
