class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for i in tokens:
            if i=='+':
                stack.append(stack.pop() + stack.pop()) 
            elif i=='-':
                j = stack.pop()
                k = stack.pop()
                stack.append(k-j) 
            elif i=='*':
                stack.append(stack.pop() * stack.pop()) 
            elif i=='/':
                j = stack.pop()
                k = stack.pop()
                stack.append(int(k/j))
            else:
                stack.append(int(i))
        
        return stack[-1]
