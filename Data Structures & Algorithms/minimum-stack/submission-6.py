class MinStack:
    # constant time for each function with n space 

    def __init__(self) -> None:
        self.min_so_far = 0
        self.stack = []
        

    def push(self, val: int) -> None:
        # maybe i should push tupled pair (val, min_so_far)
        # so if not stack, then the min so far will be the same as the val
        # if stack already have something, then we compare the min with    the val
        if not self.stack:
            self.min_so_far = val
            self.stack.append((val, self.min_so_far))
        else:
            if val < self.min_so_far:
                self.min_so_far = val
                self.stack.append((val, self.min_so_far))
            else:
                self.stack.append((val, self.min_so_far))
            

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_so_far = self.stack[-1][-1]

    def top(self) -> int:
        # this is bascailly peeking
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        # for this case, i cannot search because i need constant time
        return self.stack[-1][-1]
        
