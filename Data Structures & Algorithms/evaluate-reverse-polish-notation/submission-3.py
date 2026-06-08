class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                if tokens[i] == "+":
                    tmp = (stack[-1]+stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                elif tokens[i] == '-':
                    tmp = (stack[-2]-stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                elif tokens[i] == '*':
                    tmp = (stack[-1]*stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
                elif tokens[i] == '/':
                    tmp = int(stack[-2]/stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(tmp)
            else:
                stack.append(int(tokens[i]))
            
        return stack[-1]