class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # store indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]: # temperatures[stack[-1]] should give us the highest temperature
                pop_idx = stack.pop()
                res[pop_idx] = i - pop_idx

            
            stack.append(i) # append the idx mapped to the highest temp such that last el of stack will be the highest temp
        
        return res
        