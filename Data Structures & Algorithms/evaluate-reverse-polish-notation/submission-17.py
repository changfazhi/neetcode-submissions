class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # iterate each token, identify type and append accordingly
        # if num, just append
        # if operator, pop 2 number from stack, and then apply operator
        # the new number append back to stack
        # then return stack[0]

        operators = {"+", "-", "*", "/"}
        # base case
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                if stack:
                    right = int(stack.pop())
                    left = int(stack.pop())
                    if token == "+":
                        res = left + right
                        stack.append(int(res))
                    elif token == "-":
                        res = left - right
                        stack.append(int(res))
                    elif token == "*":
                        res = left * right
                        stack.append(int(res))
                    else:
                        res = left / right
                        stack.append(int(res))
        return stack[0]

