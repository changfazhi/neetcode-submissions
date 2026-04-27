class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) for both space and time
        # only start counting if num - 1 does not exist so that we know it is the start of a seq
        # convert the list to ict so that we can look up at O(1)
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
        
        

        