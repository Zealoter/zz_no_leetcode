# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。） 
# 
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。 
# 
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [[0,1],[1,0]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length == A[0].length <= 100 
#  A[i][j] == 0 或 A[i][j] == 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 148 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        start = []
    
        def dfs(x, y):
            if A[x][y] == 0:
                A[x][y] = -2
                start.append([x, y])
                return
            if A[x][y] == 1:
                A[x][y] = -1
            else:
                return
            if x > 0:
                dfs(x - 1, y)
            if y > 0:
                dfs(x, y - 1)
            if x < n - 1:
                dfs(x + 1, y)
            if y < m - 1:
                dfs(x, y + 1)
    
        flag = False
        for ix in range(n):
            if flag:
                break
            for iy in range(m):
                if A[ix][iy]:
                    dfs(ix, iy)
                    flag = True
                    break
    
        while start:
            now = start.pop(0)
            x = now[0]
            y = now[1]
            if x > 0:
                if A[x - 1][y] == 0:
                    A[x - 1][y] = A[x][y] - 1
                    start.append([x - 1, y])
                elif A[x - 1][y] == 1:
                    # print(-A[x][y] - 1)
                    # break
                    return -A[x][y] - 1
            if y > 0:
                if A[x][y - 1] == 0:
                    A[x][y - 1] = A[x][y] - 1
                    start.append([x, y - 1])
                elif A[x][y - 1] == 1:
                    # print(-A[x][y] - 1)
                    # break
                    return -A[x][y] - 1
            if x < n - 1:
                if A[x + 1][y] == 0:
                    A[x + 1][y] = A[x][y] - 1
                    start.append([x + 1, y])
                elif A[x + 1][y] == 1:
                    # print(-A[x][y] - 1)
                    # break
                    return -A[x][y] - 1
            if y < m - 1:
                if A[x][y + 1] == 0:
                    A[x][y + 1] = A[x][y] - 1
                    start.append([x, y + 1])
                elif A[x][y + 1] == 1:
                    # print(-A[x][y] - 1)
                    # break
                    return -A[x][y] - 1

# leetcode submit region end(Prohibit modification and deletion)
# A = [[1,0,0],[0,0,0],[0,0,1]]
# n = len(A)
# m = len(A[0])
# start = []
#
#
# def dfs(x, y):
#     if A[x][y] == 0:
#         A[x][y] = -2
#         start.append([x, y])
#         return
#     if A[x][y] == 1:
#         A[x][y] = -1
#     else:
#         return
#     if x > 0:
#         dfs(x - 1, y)
#     if y > 0:
#         dfs(x, y - 1)
#     if x < n - 1:
#         dfs(x + 1, y)
#     if y < m - 1:
#         dfs(x, y + 1)
#
#
# flag = False
# for ix in range(n):
#     if flag:
#         break
#     for iy in range(m):
#         if A[ix][iy]:
#             dfs(ix, iy)
#             flag = True
#             break
#
# while start:
#     now = start.pop(0)
#     x = now[0]
#     y = now[1]
#     if x > 0:
#         if A[x - 1][y] == 0:
#             A[x - 1][y] = A[x][y] - 1
#             start.append([x - 1, y])
#         elif A[x - 1][y] == 1:
#             print(-A[x][y]-1)
#             break
#     if y > 0:
#         if A[x][y - 1] == 0:
#             A[x][y - 1] = A[x][y] - 1
#             start.append([x, y - 1])
#         elif A[x][y - 1] == 1:
#             print(-A[x][y]-1)
#             break
#     if x < n-1:
#         if A[x + 1][y] == 0:
#             A[x + 1][y] = A[x][y] - 1
#             start.append([x + 1, y])
#         elif A[x + 1][y] == 1:
#             print(-A[x][y]-1)
#             break
#     if y < m-1:
#         if A[x][y + 1] == 0:
#             A[x][y + 1] = A[x][y] - 1
#             start.append([x, y + 1])
#         elif A[x][y + 1] == 1:
#             print(-A[x][y]-1)
#             break
