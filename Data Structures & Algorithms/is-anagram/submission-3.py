class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # should be solved iteratively as space is constant at o(1), time is n + m, so i cannot double loop
        # iterate one of them, then see if the char is in another string?
        # track each char appearance
        # edge case 1: diff len stings
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        
        