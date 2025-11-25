class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+/-*":

                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = b - a

                elif token == "*":
                    result = a * b

                elif token == "/":
                    result = int(b/a)
                    
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
            