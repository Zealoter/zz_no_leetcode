# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# 
# 输出：
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入：
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# 
# 输出：
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定矩阵的元素个数不超过 10000。 
#  给定矩阵中至少有一个元素是 0。 
#  矩阵中的元素只在四个方向上相邻: 上、下、左、右。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        start = []
    
        def dfs(x, y):
            if x > 0:
                if matrix[x - 1][y] == 1:
                    matrix[x - 1][y] = -1
                    start.append([x - 1, y])
            if y > 0:
                if matrix[x][y - 1] == 1:
                    matrix[x][y - 1] = -1
                    start.append([x, y - 1])
            if x < n - 1:
                if matrix[x + 1][y] == 1:
                    matrix[x + 1][y] = -1
                    start.append([x + 1, y])
            if y < m - 1:
                if matrix[x][y + 1] == 1:
                    matrix[x][y + 1] = -1
                    start.append([x, y + 1])
    
        for ix in range(n):
            for iy in range(m):
                if not matrix[ix][iy]:
                    dfs(ix, iy)
    
        while start:
            now = start.pop(0)
            x = now[0]
            y = now[1]
            if x > 0:
                if matrix[x - 1][y] == 1:
                    matrix[x - 1][y] = matrix[x][y] - 1
                    start.append([x - 1, y])
            if y > 0:
                if matrix[x][y - 1] == 1:
                    matrix[x][y - 1] = matrix[x][y] - 1
                    start.append([x, y - 1])
            if x < n - 1:
                if matrix[x + 1][y] == 1:
                    matrix[x + 1][y] = matrix[x][y] - 1
                    start.append([x + 1, y])
            if y < m - 1:
                if matrix[x][y + 1] == 1:
                    matrix[x][y + 1] = matrix[x][y] - 1
                    start.append([x, y + 1])
        for ix in range(n):
            for iy in range(m):
                matrix[ix][iy] = -matrix[ix][iy]
        return matrix


# leetcode submit region end(Prohibit modification and deletion)
# matrix = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
# n = len(matrix)
# m = len(matrix[0])
# start = []
#
#
# def dfs(x, y):
#     if x > 0:
#         if matrix[x - 1][y] == 1:
#             matrix[x - 1][y] = -1
#             start.append([x - 1, y])
#     if y > 0:
#         if matrix[x][y - 1] == 1:
#             matrix[x][y - 1] = -1
#             start.append([x, y - 1])
#     if x < n - 1:
#         if matrix[x + 1][y] == 1:
#             matrix[x + 1][y] = -1
#             start.append([x + 1, y])
#     if y < m - 1:
#         if matrix[x][y + 1] == 1:
#             matrix[x][y + 1] = -1
#             start.append([x, y + 1])
#
#
# for ix in range(n):
#     for iy in range(m):
#         if not matrix[ix][iy]:
#             dfs(ix, iy)
#
# while start:
#     now = start.pop(0)
#     x = now[0]
#     y = now[1]
#     if x > 0:
#         if matrix[x - 1][y] == 1:
#             matrix[x - 1][y] = matrix[x][y] - 1
#             start.append([x - 1, y])
#     if y > 0:
#         if matrix[x][y - 1] == 1:
#             matrix[x][y - 1] = matrix[x][y] - 1
#             start.append([x, y - 1])
#     if x < n - 1:
#         if matrix[x + 1][y] == 1:
#             matrix[x + 1][y] = matrix[x][y] - 1
#             start.append([x + 1, y])
#     if y < m - 1:
#         if matrix[x][y + 1] == 1:
#             matrix[x][y + 1] = matrix[x][y] - 1
#             start.append([x, y + 1])
# for ix in range(n):
#     for iy in range(m):
#         matrix[ix][iy] = -matrix[ix][iy]
# print(matrix)
