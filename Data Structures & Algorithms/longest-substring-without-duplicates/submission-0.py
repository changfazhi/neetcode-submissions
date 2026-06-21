class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        
        # mapping should be using a dict, i need a freqmap to see if any of their value is more than 1
        mapper = {}
        best = 0
        for right in range(0, len(s)):
            mapper[s[right]] = mapper.get(s[right], 0) + 1
            # now i should be checking if the window is valid or nah
            # to do so, if a char already exist in set means it aint vaild
            while mapper[s[right]] > 1:
                mapper[s[left]] -= 1
                if mapper[s[left]] == 0:
                    del mapper[s[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
            
        