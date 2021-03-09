

# 使用一个栈来模拟
# 首先根据弹出序列判断压入哪些元素
# 如果栈顶元素不等于弹出序列，则需要继续压入元素
# 如果相等，则弹出，弹出序列向后判定

def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = ['#']
    i,j = 0,0
    while j<len(popped):
        #print(stack)
        if stack[-1] != popped[j]:
            if i<len(pushed):
                stack.append(pushed[i])
                i += 1
            else:
                return False
        else:
            stack.pop(-1)
            j += 1
    return True 