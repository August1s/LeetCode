

def romanToInt(s: str) -> int:
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i=0
    result = 0
    while i!=len(s):
        if i == len(s)-1 or dic[s[i]] >= dic[s[i+1]]:
            result += dic[s[i]]
            i += 1
        else:
            result += dic[s[i+1]]-dic[s[i]]
            i += 2
    return result

print(romanToInt("LVIII"))

        

