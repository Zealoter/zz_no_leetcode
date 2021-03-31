# 给定一个二叉树，在树的最后一行找到最左边的值。 
# 
#  示例 1: 
# 
#  
# 输入:
# 
#     2
#    / \
#   1   3
# 
# 输出:
# 1
#  
# 
#  
# 
#  示例 2: 
# 
#  
# 输入:
# 
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# 
# 输出:
# 7
#  
# 
#  
# 
#  注意: 您可以假设树（即给定的根节点）不为 NULL。 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        start=[root]
        ans=root.val
        while start:
            now_node=start.pop(0)
            if now_node.right:
                start.append(now_node.right)
                ans=now_node.right.val
            if now_node.left:
                start.append(now_node.left)
                ans=now_node.left.val
            
        return ans
# leetcode submit region end(Prohibit modification and deletion)
