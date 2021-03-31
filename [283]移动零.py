# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 991 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        len_num = len(nums)
        len_num_tmp = len_num
        while i < len_num_tmp:
            if nums[i] == 0:
                nums.pop(i)
                len_num_tmp -= 1
            else:
                i += 1
        for _ in range(len_num_tmp, len_num):
            nums.append(0)
# leetcode submit region end(Prohibit modification and deletion)
