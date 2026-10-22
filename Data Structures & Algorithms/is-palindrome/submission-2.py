class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        # 2 pointers, one left, one right
        # it will converge to the center 
        # at each, check if it is the same alphanum
        # before that check if it is even an alphanum, if not skip by moving pointer

        while l < r:
            # check alphanum
            if s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -= 1
            # check if it is the same alphanum
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
        
        return True
        