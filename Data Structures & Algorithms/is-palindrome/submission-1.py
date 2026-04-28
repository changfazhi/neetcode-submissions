class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip("").lower()
        s = "".join(c for c in s if c.isalnum())
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True
