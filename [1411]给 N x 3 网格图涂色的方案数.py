# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜
# 色不同）。 
# 
#  给你网格图的行数 n 。 
# 
#  请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：12
# 解释：总共有 12 种可行的方法：
# 
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：54
#  
# 
#  示例 3： 
# 
#  输入：n = 3
# 输出：246
#  
# 
#  示例 4： 
# 
#  输入：n = 7
# 输出：106494
#  
# 
#  示例 5： 
# 
#  输入：n = 5000
# 输出：30228214
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  grid[i].length == 3 
#  1 <= n <= 5000 
#  
#  Related Topics 动态规划 
#  👍 77 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfWays(self, n: int) -> int:
        n -= 1
        a = 1
        b = 1
        while n:
            n -= 1
            a, b = 3 * a + 2 * b, 2 * a + 2 * b
            a %= 1000000007
            b %= 1000000007
        return (6 * a + 6 * b) % 1000000007
# class Solution:
#     def numOfWays(self, n: int) -> int:
#         ans = [1] * 12
#         tans = {
#             0: [1, 2, 4, 5, 10],
#             1: [0, 3, 6, 8, 11],
#             2: [0, 3, 6, 7],
#             3: [1, 2, 7, 10],
#             4: [0, 6, 8, 9],
#             5: [0, 6, 7, 9, 10],
#             6: [1, 2, 4, 5, 11],
#             7: [2, 3, 5, 11],
#             8: [1, 4, 9, 10],
#             9: [4, 5, 8, 11],
#             10: [0, 3, 5, 8, 11],
#             11: [1, 6, 7, 9, 10],
#         }
#         while n:
#             tmp = [0] * 12
#             for i in range(12):
#                 for can_next in tans[i]:
#                     tmp[can_next] += ans[-1][i]
#             ans = tmp
#             n -= 1
# n=7
# ans = [1] * 12
# tans = {
#     0: [1, 2, 4, 5, 10],
#     1: [0, 3, 6, 8, 11],
#     2: [0, 3, 6, 7],
#     3: [1, 2, 7, 10],
#     4: [0, 6, 8, 9],
#     5: [0, 6, 7, 9, 10],
#     6: [1, 2, 4, 5, 11],
#     7: [2, 3, 5, 11],
#     8: [1, 4, 9, 10],
#     9: [4, 5, 8, 11],
#     10: [0, 3, 5, 8, 11],
#     11: [1, 6, 7, 9, 10],
# }
# n-=1
# while n:
#     tmp = [0] * 12
#     for i in range(12):
#         for can_next in tans[i]:
#             tmp[can_next] += ans[i]
#     ans = tmp
#     n -= 1
#     print(ans)
# print(sum(ans))
# n = 5000
# n -= 1
# a = 1
# b = 1
# while n:
#     n -= 1
#     a, b = 3 * a + 2 * b, 2 * a + 2 * b
#     a %= 1000000007
#     b %= 1000000007
# print((6 * a + 6 * b) % 1000000007)
# leetcode submit region end(Prohibit modification and deletion)
