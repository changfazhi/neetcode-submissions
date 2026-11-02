class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        stack = []
        res = []
        for i in range(n):
            stack.append((position[i], speed[i]))
        # so now the stack is filled with (position, speed)
        stack.sort(key=lambda x: x[0], reverse = True)
        # now this is sorted by position

        # car cannot overtake 
        # we need to find the time taken for each car to reach the destination if car can overtake

        m = len(stack)
        for j in range(m):
            pos = stack[j][0]
            spd = stack[j][-1]
            reach = (pos - target) / spd # this is the time to reach the target
            # monotonic decreaasing stack
            # if i take longer, then i will be in a different fleet
            # if i take short, then i will merge with the fleet infront of me
            if not res or res[-1] > reach:
                res.append(reach)
        
        return len(res)
