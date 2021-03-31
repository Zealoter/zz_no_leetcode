# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#  
#  👍 220 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def judge(l, r, num):
            tmp = l
            if r <= l:
                return True
            while postorder[tmp] < num and tmp <= r:
                tmp += 1
            if r <= tmp:
                return judge(l, r - 1, postorder[r])

            e = tmp - 1
            while tmp <= r:
                if postorder[tmp] < num:
                    return False
                tmp += 1
            return judge(l, e - 1, postorder[e]) and judge(e + 1, r - 1, postorder[r])

        if not postorder:
            return True
        return judge(0, len(postorder) - 2, postorder[-1])

# leetcode submit region end(Prohibit modification and deletion)
# postorder = [5, 2, -17, -11, 25, 76, 62, 98, 92, 61]
#
#
# def judge(l, r, num):
#     tmp = l
#     if r <= l:
#         return True
#     while postorder[tmp] < num and tmp <= r:
#         tmp += 1
#     if r <= tmp:
#         return judge(l, r-1, postorder[r])
#
#     e = tmp - 1
#     while tmp <= r:
#         if postorder[tmp] < num:
#             return False
#         tmp += 1
#     return judge(l, e - 1, postorder[e]) and judge(e + 1, r - 1, postorder[r])
#
#
# print(judge(0, len(postorder) - 2, postorder[-1]))
