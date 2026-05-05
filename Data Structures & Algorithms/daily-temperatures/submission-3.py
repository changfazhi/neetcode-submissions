class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) time and O(n) space
        # need stack data structure
        # as iterate thru, add temp to stack
        # if wtv i add is more than the bottom, count len(stack) - 1 and append to res
        # then remove btm
        res = [0] * len(temperatures)
        stack = [] # [temp, idx]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, idxT = stack.pop()
                res[idxT] = i - idxT
            stack.append((t, i))
        return res
       
        