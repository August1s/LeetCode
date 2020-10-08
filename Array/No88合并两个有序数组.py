
'''
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
'''


def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p, q, r = m-1, n-1, m + n -1
        while(r >= 0):
            if p < 0:
                nums1[r] = nums2[q]
                q -= 1
            elif q < 0:
                nums1[r] = nums1[p]
                p -= 1
            else:
                if nums1[p] > nums2[q]:
                    nums1[r] = nums1[p]
                    p -= 1
                else:
                    nums1[r] = nums2[q]
                    q -= 1
            r -= 1    


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3
print(merge(nums1,m,nums2,n))