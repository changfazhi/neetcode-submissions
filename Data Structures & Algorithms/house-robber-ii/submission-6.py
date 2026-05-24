class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) for space and time
        # edge case
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        memo1 = [-1] * len(nums1)

        nums2 = nums[:-1]
        memo2 = [-1] * len(nums2)

        def dfs1(i):
            # base case
            if i >= len(nums1):
                return 0

            if memo1[i] != -1:
                return memo1[i]

            max_money1 = 0
            # recurrence relation
            if max_money1 < max(nums1[i] + dfs1(i+2), dfs1(i+1)):
                max_money1 = max(nums1[i] + dfs1(i+2), dfs1(i+1))
            memo1[i] = max_money1
            return memo1[i]

        def dfs2(i):
            # base case
            if i >= len(nums2):
                return 0

            if memo2[i] != -1:
                return memo2[i]

            max_money2 = 0
            # recurrence relation
            if max_money2 < max(nums2[i] + dfs2(i+2), dfs2(i+1)):
                max_money2 = max(nums2[i] + dfs2(i+2), dfs2(i+1))
            memo2[i] = max_money2
            return memo2[i]

        return max(dfs1(0), dfs2(0))