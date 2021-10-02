# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。 
# 
#  注意: 
# 
#  
#  十六进制中所有字母(a-f)都必须是小写。 
#  十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
#  给定的数确保在32位有符号整数范围内。 
#  不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。 
#  
# 
#  示例 1： 
# 
#  
# 输入:
# 26
# 
# 输出:
# "1a"
#  
# 
#  示例 2： 
# 
#  
# 输入:
# -1
# 
# 输出:
# "ffffffff"
#  
#  Related Topics 位运算 数学 👍 183 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        Hex = '0123456789abcdef'
        res = ''
        while len(res) < 8 and num:
            res += Hex[0b1111 & num]
            num >>= 4
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
