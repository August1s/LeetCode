
# 二维数组的每一行递增，每一列递增，但是如果将这个数组旋转45度，就会发现他是一个类似与搜索树的结构
#[
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#    
#
#
    #     15
    #   11  19
    # 7   12  22
    #     ...
# 这样就可以按照二叉搜索树的策略进行搜索

def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    if matrix == [] or matrix == [[]]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    i, j = 0, n-1
    while i!=m and j!=-1:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False