class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) time and O(1) space
        # using 2 pointers, first pointer remain, second pointer explore and check for more information
        # if second pointer returns nothing for target, move first pointer by 1, second pointer start from pointer 1 + 1
        p1 = 0
        p2 = 1
        res = []
        # best case
        

        while numbers[p1] + numbers[p2] != target:
            p2 += 1
            if p2 == len(numbers):
                p1 += 1
                p2 = p1 + 1
            else:
                continue
        
        if numbers[p1] + numbers[p2] == target:
            res.append(p1 + 1)
            res.append(p2 + 1)
            return res

        