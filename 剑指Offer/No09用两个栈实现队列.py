

# stack1负责入队，stack2负责出队
# 当stack2为空的时候，将stack1倒入stack2中，然后再出队即可



def __init__(self):
    self.stack1 = []
    self.stack2 = []

def appendTail(self, value: int) -> None:
    self.stack1.append(value)


def deleteHead(self) -> int:
    if self.stack1==[] and self.stack2==[]:
        return -1
    elif self.stack2 == []:
        while self.stack1!=[]:
            self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)
    else:
        return self.stack2.pop(-1)