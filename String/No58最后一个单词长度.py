    
def lengthOfLastWord(s: str) -> int:
    res = s.split(" ")
    if len(res) == 0:
        return 0
    for i in range(len(res)-1, -1, -1):
        if len(res[i]) != 0:
            return len(res[i])
    return 0


print(lengthOfLastWord(" qq  "))