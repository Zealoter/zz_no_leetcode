# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。 
# 
#  我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。 
# 
#  如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。 
# 
#  请返回封闭岛屿的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1
# ,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
#  Related Topics 深度优先搜索 
#  👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
	def closedIsland(self, grid: List[List[int]]) -> int:
		n = len(grid)
		m = len(grid[0])

		def dfs(x, y):
			if grid[x][y]:
				return
			else:
				grid[x][y] = 1
			if x < n - 1:
				dfs(x + 1, y)
			if x > 0:
				dfs(x - 1, y)
			if y < m - 1:
				dfs(x, y + 1)
			if y > 0:
				dfs(x, y - 1)

		for i in range(n):
			if not grid[i][0]:
				dfs(i, 0)
			if not grid[i][m - 1]:
				dfs(i, m - 1)

		for j in range(m):
			if not grid[0][j]:
				dfs(0, j)
			if not grid[n - 1][j]:
				dfs(n - 1, j)
		ans = 0
		for i in range(1, n - 1):
			for j in range(1, m - 1):
				if not grid[i][j]:
					ans += 1
					dfs(i, j)

		return ans

# leetcode submit region end(Prohibit modification and deletion)
# grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
#         [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
#         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
#         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
# n = len(grid)
# m = len(grid[0])
#
#
# def dfs(x, y):
# 	if grid[x][y]:
# 		return
# 	else:
# 		grid[x][y] = 1
# 	if x < n - 1:
# 		dfs(x + 1, y)
# 	if x > 0:
# 		dfs(x - 1, y)
# 	if y < m - 1:
# 		dfs(x, y + 1)
# 	if y > 0:
# 		dfs(x, y - 1)
#
#
# for i in range(n):
# 	if not grid[i][0]:
# 		dfs(i, 0)
# 	if not grid[i][m - 1]:
# 		dfs(i, m - 1)
#
# for j in range(m):
# 	if not grid[0][j]:
# 		dfs(0, j)
# 	if not grid[n - 1][j]:
# 		dfs(n - 1, j)
# ans = 0
# for i in range(1, n - 1):
# 	for j in range(1, m - 1):
# 		if not grid[i][j]:
# 			ans += 1
# 			dfs(i, j)
# print(ans)
