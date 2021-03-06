# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length <= 40000 
#  
# 
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/ 
#  Related Topics 哈希表 双指针 Sliding Window 
#  👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i1 = 0
        i2 = 0
        c = set()
        s_len = len(s)
        if s_len == 0:
            return 0
        ans = 1
        while i1 < s_len:
            if s[i1] in c:
                while s[i2] != s[i1]:
                    c.remove(s[i2])
                    i2 += 1
                i2 += 1
            else:
                c.add(s[i1])
            i1 += 1
            if i1 - i2 > ans:
                ans = i1 - i2
        return ans  # leetcode submit region end(Prohibit modification and deletion)
