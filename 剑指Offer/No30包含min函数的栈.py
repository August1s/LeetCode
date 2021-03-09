
# 这道题的关键是在O(1)时间内找最小值
# 可以通过维护一个栈来存储最小值


def __init__(self):
    self.stack = []
    self.minstack = [float('inf')]


def push(self, x: int) -> None:
    self.stack.append(x)
    if x<=self.minstack[-1]:
        self.minstack.append(x)

def pop(self) -> None:
    r = self.stack.pop(-1)
    if r==self.minstack[-1]:
        self.minstack.pop(-1)

def top(self) -> int:
    return self.stack[-1]


def min(self) -> int:
    return self.minstack[-1]