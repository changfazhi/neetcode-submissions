class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char in mapping: # if its closing
                top_el = stack.pop() if stack else "#" # take out the top el which is an opening

                if top_el != mapping[char]: # if the closing does not match the opening, then return false
                    return False
            else: # if its opening
                stack.append(char)
        
        # if the length of stack is cleared, this means that it is valid
        return len(stack) == 0
