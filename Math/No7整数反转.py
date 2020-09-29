


def reverse(x: int) -> int:
    if x<-2**31 or x>2**31:
        return 0
    if x>0:
        a = int(str(x)[::-1])
        return 0 if a<-2**31 or a>2**31 else a
    else:
        a = int('-'+str(-x)[::-1])
        return 0 if a<-2**31 or a>2**31 else a

x = 1534236469
print(reverse(x))
