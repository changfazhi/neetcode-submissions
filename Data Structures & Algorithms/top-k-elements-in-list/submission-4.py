class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time is O(n) and space is O(n)
        # need count to track how many time a num appears
        # create a freq table, store the num based on how many time it appears
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # store the num based on how many time it appears in freq
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # iterate backwards, append res until len(res) == k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res


        
        
        

            
        
       
