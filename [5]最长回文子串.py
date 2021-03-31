# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 3365 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[0] * s_len for _ in range(s_len)]
        ans = 1
        ans_str=s[0]
        for tmp_i in range(s_len):
            dp[tmp_i][tmp_i] = 1
        for ii in range(s_len - 1):
            for jj in range(1, s_len - ii):
                i = jj - 1
                j = ii + jj
                if s[i] == s[j] and i + 1 == j:
                    dp[i][j] = 2
                    if 2 > ans:
                        ans = 2
                        ans_str = s[i:j+1]
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > ans:
                        ans = dp[i][j]
                        ans_str = s[i:j + 1]
        return ans_str
# leetcode submit region end(Prohibit modification and deletion)
# s = 'baabad'
# s_len = len(s)
# # 0 for i in range(s_len)
# dp = [[0] * s_len for _ in range(s_len)]
# ans = 1
# for tmp_i in range(s_len):
#     dp[tmp_i][tmp_i] = 1
# for ii in range(s_len - 1):
#     for jj in range(1, s_len - ii):
#         i = jj - 1
#         j = ii + jj
#         if s[i] == s[j] and i + 1 == j:
#             dp[i][j] = 2
#             if 2 > ans:
#                 ans = 2
#         if dp[i + 1][j - 1] and s[i] == s[j]:
#             dp[i][j] = dp[i + 1][j - 1] + 2
#             if dp[i][j] > ans:
#                 ans = dp[i][j]
#
# print(ans)
