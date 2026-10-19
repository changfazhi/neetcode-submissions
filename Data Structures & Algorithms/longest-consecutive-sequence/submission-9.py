class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        length = 0

        # make everything into a set so that all the numbers are unique
        # we need to start counting from every start of the sequence 
        # then use max to change the longest
        for num in numSet:
            # check for behind to see if it is the start of a sequence
            if (num - 1) not in numSet: # this is the start of a sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                
            longest = max(longest, length)
        
        return longest
            
        