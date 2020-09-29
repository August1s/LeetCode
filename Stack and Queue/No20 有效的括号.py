

# 利用栈来匹配括号，相邻一对括号就出栈，判断是否为空栈来判断括号是否匹配
'''
def isValid(s: str) -> bool:
    L = []
    for i in s:
        L.append(i)
        if len(L) == 1:
            continue
        index = len(L)-1
        if L[index-1]+L[index] == '[]' or L[index-1]+L[index] == '{}' or L[index-1]+L[index] == '()':
            L.pop()
            L.pop()
    return True if len(L) == 0 else False'''

def isValid(s: str) -> bool:
    dic = {'{': '}',  '[': ']', '(': ')','?':'?'}
    # 问号是为了防止空栈
    L = ['?']
    for i in s:
        # 在字符入栈前就可以判断，如果字符为左括号则直接入栈
        # 如果为右括号，可以直接判断栈顶括号是否匹配，这样右括号不用入栈
        # 当括号不匹配时，可以直接提前返回
        if i in dic.keys():
            L.append(i)
        elif dic[L.pop()] != i: 
            return False
    return len(L) == 1


print(isValid(""))

