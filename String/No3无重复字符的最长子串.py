


# 无重复最长字串可以使用滑动窗口

'''
def lengthOfLongestSubstring(s: str) -> int:
    if not s:return 0
    left = 0
    lookup = set() # 用set的长度来判断重复，也可以使用list和dict
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])  # s[i]在lookup中，说明有重复。
            left += 1  # 滑动窗口右移，删去元素，直到没有重复为止
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])
    return max_len'''
'''
def lengthOfLongestSubstring(s: str) -> int:
    if not s:return 0
    lookup = [] # list中储存了无重子串
    max_len = 0
    for i in s:
        if not i in lookup:
            lookup.append(i)
        else:
            left = lookup.index(i)
            lookup = lookup[left+1:] # 用切片可以不用写循环
            lookup.append(i)
        max_len = max(max_len,len(lookup))
    return max_len'''
'''
# 可以用双指针记录字串的头尾位置，可以少创建一个记录无重字串的数组
def lengthOfLongestSubstring(s: str) -> int:
    if not s:return 0
    p,q = 0,0 # 记录字符串头尾
    max_len = 0
    for i in s:
        if not i in s[p:q]:
            q += 1
        else:
            p += s[p:q].index(i)+1 
            q += 1
        max_len = max(max_len,q-p)
    return max_len'''

# index()的复杂度是n，所以可以用dict来判断
def lengthOfLongestSubstring(s: str) -> int:
    if not s:return 0
    dic = {}
    max_len = 0
    start = -1 # 最大子串的起始位置-1
    for index,i in enumerate(s):
        if i in dic and dic[i]>start:
            start = dic[i]
        max_len = max(max_len,index-start)
        dic[i] = index
    return max_len


s="beabb"
print(lengthOfLongestSubstring(s))