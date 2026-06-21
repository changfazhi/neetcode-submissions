class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        best = 0
        mapping = {}
        maxf = 0
        # its only valid if i have 1 distinct char + 2nd distinct char but it cannot appear more than k
        for right in range(len(s)):
            mapping[s[right]] = mapping.get(s[right], 0) + 1
            maxf = max(maxf, mapping[s[right]])

            window_length = right - left + 1
            # while not valid, i need to decrease my window size
            if window_length - maxf > k:
                mapping[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        
        return best



        