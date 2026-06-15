class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # cannot use a hashmap because i need to solve it in constant space
        uniqueNum = set()
        # create a set to store all unique numbers i have encountered so far
        # i will then check the set, if not there add to the set else i will return the int
        for num in nums:
            if num not in uniqueNum:
                uniqueNum.add(num)
            else:
                return num
        