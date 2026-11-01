class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # stack that stores indices
        # monotonic decreasing stack

        for i,temp in enumerate(temperatures):
            # start stacking
            while stack and temperatures[stack[-1]] < temp:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res 
