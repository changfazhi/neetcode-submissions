class Solution:
    def isValid(self, s: str) -> bool:
        # i need to have a stack as this question is about FIFO
        # use the stack to store the opening and pop them when needed
        # iterate s, if open, store in stack
        # if close, if match with stack, pop it
        # if close and does not match, return false
        # at the end of the iteration, if stack is not empty, return false
        stack = []
        hashMatch = {")": "(",
                    "}": "{",
                    "]": "["}

        for c in s:
            # opening
            if c in hashMatch.values():
                stack.append(c)
            # closing
            if c in hashMatch:
                if stack and hashMatch[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        
        if stack:
            return False
        else:
            return True

        