class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time and O(n) space
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            else:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True
