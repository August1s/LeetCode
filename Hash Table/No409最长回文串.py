
# 使用一个hashmap记录所有字母出现的次数
# 偶数次直接加，奇数次除第一个奇数以外需要减1再加
def longestPalindrome(self, s: str) -> int:
    hashmap = {}
    for i in s:
        if not i in hashmap.keys():
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    count = 0
    first = False
    for i in hashmap.keys():
        if hashmap[i]%2==0:
            count+=hashmap[i]
        else:
            if not first:
                count += hashmap[i]
                first = True
            else:
                count += hashmap[i]-1

    return count