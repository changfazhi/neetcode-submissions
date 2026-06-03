class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first of all, sort the car
        cars = sorted(zip(position, speed), reverse = True)

        stack = [] # store the arrival time of the cars

        for pos, spd in cars:
            time = (target - pos) / spd
            # need to see the time needed to reach the target
            # stack[-1] is the fleet ahead, we need to see if we are faster or slower
            # if faster we can join the fleet, if slower we will be in another fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)