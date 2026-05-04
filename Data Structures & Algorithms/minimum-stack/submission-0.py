class MinStack:
    # O(1) time for each function call and O(n) space
    
    def __init__(self):
        self.stackList = []

    def push(self, val: int) -> None:
        self.stackList.append(val)

    def pop(self) -> None:
        self.stackList.pop(-1)

    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return min(self.stackList)
