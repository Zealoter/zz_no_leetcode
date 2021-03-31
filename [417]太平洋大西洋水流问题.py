# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。 
# 
#  规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。 
# 
#  请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。 
# 
#  
# 
#  提示： 
# 
#  
#  输出坐标的顺序不重要 
#  m 和 n 都小于150 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 给定下面的 5x5 矩阵:
# 
#   太平洋 ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        tmp_p = [[0] * n for i in range(m)]
        self.ans = []

        def dfs(x, y):
            if tmp_p[x][y] == 1:
                return
            tmp_p[x][y] = 1
            if x > 0 and heights[x][y] <= heights[x - 1][y]:
                dfs(x - 1, y)
            if x < m - 1 and heights[x][y] <= heights[x + 1][y]:
                dfs(x + 1, y)
            if y > 0 and heights[x][y] <= heights[x][y - 1]:
                dfs(x, y - 1)
            if y < n - 1 and heights[x][y] <= heights[x][y + 1]:
                dfs(x, y + 1)

        def dfs2(x, y):
            if tmp_p[x][y] == 2 or tmp_p[x][y] == 3:
                return
            tmp_p[x][y] += 2
            if tmp_p[x][y] == 3:
                self.ans.append([x, y])


            if x > 0 and heights[x][y] <= heights[x - 1][y]:
                dfs2(x - 1, y)
            if x < m - 1 and heights[x][y] <= heights[x + 1][y]:
                dfs2(x + 1, y)
            if y > 0 and heights[x][y] <= heights[x][y - 1]:
                dfs2(x, y - 1)
            if y < n - 1 and heights[x][y] <= heights[x][y + 1]:
                dfs2(x, y + 1)

        for i in range(m):
            dfs(i, 0)
        for j in range(n):
            dfs(0, j)
        for i in range(m):
            dfs2(i, n - 1)
        for j in range(n):
            dfs2(m - 1, j)
        return self.ans

# leetcode submit region end(Prohibit modification and deletion)
# heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# m = len(heights)
# n = len(heights[0])
# tmp_p = [[0] * n for i in range(m)]
# ans = []
#
#
# def dfs(x, y):
#     if tmp_p[x][y] == 1:
#         return
#     tmp_p[x][y] = 1
#     if x > 0 and heights[x][y] <= heights[x - 1][y]:
#         dfs(x - 1, y)
#     if x < m - 1 and heights[x][y] <= heights[x + 1][y]:
#         dfs(x + 1, y)
#     if y > 0 and heights[x][y] <= heights[x][y - 1]:
#         dfs(x, y - 1)
#     if y < n - 1 and heights[x][y] <= heights[x][y + 1]:
#         dfs(x, y + 1)
#
#
# def dfs2(x, y):
#     if tmp_p[x][y] == 2 or tmp_p[x][y] == 3:
#         return
#     tmp_p[x][y] += 2
#     if tmp_p[x][y] == 3:
#         ans.append([x, y])
#
#     if x > 0 and heights[x][y] <= heights[x - 1][y]:
#         dfs2(x - 1, y)
#     if x < m - 1 and heights[x][y] <= heights[x + 1][y]:
#         dfs2(x + 1, y)
#     if y > 0 and heights[x][y] <= heights[x][y - 1]:
#         dfs2(x, y - 1)
#     if y < n - 1 and heights[x][y] <= heights[x][y + 1]:
#         dfs2(x, y + 1)
#
#
# for i in range(m):
#     dfs(i, 0)
# for j in range(n):
#     dfs(0, j)
# for i in range(m):
#     dfs2(i, n - 1)
# for j in range(n):
#     dfs2(m - 1, j)
# print(ans)