class MinStack:

    def __init__(self):
        self.stack_all = []
        self.stack_min = []


    def push(self, val: int) -> None:
        if len(self.stack_min) != 0:
            self.stack_min.append(min(val, self.stack_min[-1]))
        else: 
            self.stack_min.append(val)
        self.stack_all.append(val)

    def pop(self) -> None:
        self.stack_min.pop()
        self.stack_all.pop()

    def top(self) -> int:
        return self.stack_all[-1]


    def getMin(self) -> int:
        return self.stack_min[-1]
