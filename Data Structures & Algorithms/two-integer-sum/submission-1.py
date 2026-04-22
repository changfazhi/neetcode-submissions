class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # space is n and time is n 
        # i can only iterate once,
        # if i am given n space, i think can create another list of some sort?
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    minimum = min(i,j)
                    maximum = max(i,j)
                    res.append(minimum)
                    res.append(maximum)
                    return res



        