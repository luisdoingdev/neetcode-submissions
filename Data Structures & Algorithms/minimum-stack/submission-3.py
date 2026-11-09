class MinStack:

    def __init__(self):
        self.val = []
        self.minimum = None
        

    def push(self, val: int) -> None:
        self.val.append(val)
        self.minimum = min(self.val)

    def pop(self) -> None:
        self.val.pop()
        if self.val:
            self.minimum = min(self.val)
        self.minum = None

    def top(self) -> int:
        return self.val[-1]
        
    def getMin(self) -> int:
        return self.minimum 
            

