# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#  
# 
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2
# , 1, 1, 0, 0]。 
# 
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。 
#  Related Topics 栈 哈希表 
#  👍 686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            temperature = T[i]
            while stack and T[stack[-1]] < temperature:
                preIndex = stack.pop()
                ans[preIndex] = i - preIndex
            stack.append(i)
        return ans
        # day = []
        # ans = [0] * len(T)
        # for i in range(len(T)):
        #     while day:
        #         if T[i] > day[-1][1]:
        #             ans[day[-1][0]] = i - day[-1][0]
        #             day.pop(-1)
        #         else:
        #             break
        #     day.append([i, T[i]])
        # return ans
# T = [73, 74, 75, 71, 69, 72, 76, 73]
# day = []
# ans = [0] * len(T)
# for i in range(len(T)):
#     while day:
#         if T[i] > day[-1][1]:
#             ans[day[-1][0]] = i - day[-1][0]
#             day.pop(-1)
#         else:
#             break
#     day.append([i, T[i]])
# print(ans)
# leetcode submit region end(Prohibit modification and deletion)
