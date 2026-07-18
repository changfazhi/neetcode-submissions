class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            # i need to change the number to base 2 and count the number of 1 in the base 2 form
            while i:
                count += 1
                i &= (i-1)
            res.append(count)
        
        return res
        