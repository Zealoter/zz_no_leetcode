# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。 
# 
#  示例: 
# 
#  输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
#  
#  Related Topics 数学 动态规划 回溯算法 
#  👍 129 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            ans=1
        elif n == 1:
            ans = 10
        elif n == 2:
            ans = 10 + 9 * 9
        elif n > 10:
            ans = 0
        else:
            ans = 10 + 9 * 9
            tmp = 9 * 9
            for i in range(3, n + 1):
                tmp *= (11 - i)
                ans += tmp
        return ans
# leetcode submit region end(Prohibit modification and deletion)
