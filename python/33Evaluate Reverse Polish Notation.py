class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b+a))
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b-a))
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b*a))
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))

                case _: stack.append(int(i))
        return stack.pop()