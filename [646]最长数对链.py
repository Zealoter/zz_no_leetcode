# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。 
# 
#  现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。 
# 
#  给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：[[1,2], [2,3], [3,4]]
# 输出：2
# 解释：最长的数对链是 [1,2] -> [3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给出数对的个数在 [1, 1000] 范围内。 
#  
#  Related Topics 动态规划 
#  👍 153 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        len_pairs = len(pairs)
        pairs.sort(key=lambda x: x[0])
        dp = [1] * (len_pairs)
        for i in range(1, len_pairs):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
# pairs=[[1,2], [2,3], [3,4]]
# len_pairs = len(pairs)
# pairs.sort(key=lambda x: x[0])
# dp = [1] * (len_pairs)
# for i in range(1, len_pairs):
#     for j in range(i):
#         if pairs[j][1] < pairs[i][0]:
#             dp[i] = max(dp[i], dp[j] + 1)
