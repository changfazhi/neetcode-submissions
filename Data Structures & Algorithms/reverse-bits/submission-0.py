class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # grab the rightmost bit
            bit = n & 1
            # shift the res to the left and add the bit
            res = (res << 1) | bit
            # shift the n to the right to expose the next bit
            n >>= 1
        
        return res
        