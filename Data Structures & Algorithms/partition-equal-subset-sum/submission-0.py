class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time space must be n * t
        # t is half the sum of the array elements
        # 0/1 knapsack => as i can only use each element in nums once only 

        # find target
        total = sum(nums)
        target = total // 2

        # base case is that if the total is odd, it is impossible
        if total % 2 != 0:
            return False
        
        # make the 1d-dp using a list which should consist of all false with a length of target + 1
        dp = [False] * (target + 1)
        # base case is that it is possible for me to make 0
        dp[0] = True

        # so i should iterate each num in nums then find backwards so i can see if subset can equal to num to target, target being the maximum value
        for num in nums:
            for w in range(target, num-1, -1): # iterate from num-1 to target 
                dp[w] = dp[w] or dp[w-num]
                # i want to eventually iterate till target to see if i can find a subset to hit target 
        
        return dp[target]