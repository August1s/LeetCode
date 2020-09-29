def plusOne(digits: list) -> list:
    i, c = len(digits)-1, 0
    while i>=0:
        if i == len(digits)-1:
            digits[i],c = (digits[i]+1+c)%10, (digits[i]+1+c)//10
        else:
            digits[i],c = (digits[i]+c)%10, (digits[i]+c)//10
        if i == 0:
             if c>0:
                digits = [c] + digits
        i -= 1
    return digits


#print(plusOne([1,2,3]))






