# 您需要在二叉树的每一行中找到最大的值。 
# 
#  示例： 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# 输出: [1, 3, 9]
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 126 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        start = [[root, 0]]
        ans = [root.val]
        while start:
            now_node = start.pop(0)
            if now_node[1] + 1 > len(ans):
                ans.append(now_node[0].val)
            else:
                ans[now_node[1]] = max(ans[now_node[1]], now_node[0].val)
            if now_node[0].right:
                start.append([now_node[0].right, now_node[1] + 1])
            if now_node[0].left:
                start.append([now_node[0].left, now_node[1] + 1])
        
        return ans

# leetcode submit region end(Prohibit modification and deletion)
