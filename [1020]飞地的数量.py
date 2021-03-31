# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。 
# 
#  移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。 
# 
#  返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释： 
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。 
# 
#  示例 2： 
# 
#  输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 500 
#  1 <= A[i].length <= 500 
#  0 <= A[i][j] <= 1 
#  所有行的大小都相同 
#  
#  Related Topics 深度优先搜索 
#  👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
	def numEnclaves(self, grid: List[List[int]]) -> int:
		n = len(grid)
		m = len(grid[0])
		
		def dfs(x, y):
			if not grid[x][y]:
				return
			else:
				grid[x][y] = 0
			if x < n - 1:
				dfs(x + 1, y)
			if x > 0:
				dfs(x - 1, y)
			if y < m - 1:
				dfs(x, y + 1)
			if y > 0:
				dfs(x, y - 1)
		
		for i in range(n):
			if grid[i][0]:
				dfs(i, 0)
			if grid[i][m - 1]:
				dfs(i, m - 1)
		
		for j in range(m):
			if grid[0][j]:
				dfs(0, j)
			if grid[n - 1][j]:
				dfs(n - 1, j)
		ans = 0
		for i in range(1, n - 1):
			ans += sum(grid[i])
		return ans

# leetcode submit region end(Prohibit modification and deletion)
# grid = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
# n = len(grid)
# m = len(grid[0])
#
#
# def dfs(x, y):
# 	if not grid[x][y]:
# 		return
# 	else:
# 		grid[x][y] = 0
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
# 	if grid[i][0]:
# 		dfs(i, 0)
# 	if grid[i][m - 1]:
# 		dfs(i, m - 1)
#
# for j in range(m):
# 	if grid[0][j]:
# 		dfs(0, j)
# 	if grid[n - 1][j]:
# 		dfs(n - 1, j)
# ans = 0
# for i in range(1, n - 1):
# 	ans += sum(grid[i])
# print(ans)
