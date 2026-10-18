class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for num in nums:
            if num in dupes:
                return True
            else:
                dupes.add(num)
        
        return False
        