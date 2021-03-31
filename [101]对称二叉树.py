# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 1306 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(a, b):
            if a.val != b.val:
                return False

            if not a.right and not b.left:
                pass
            if not a.left and not b.right:
                pass
            if not a.right and b.left:
                return False
            if a.right and not b.left:
                return False
            if not a.left and b.right:
                return False
            if a.left and not b.right:
                return False
            if a.left and b.right:
                if not dfs(a.left, b.right):
                    return False
            if a.right and b.left:
                if not dfs(a.right, b.left):
                    return False
            return True

        if not root:
            return True
        if root.left and root.right:
            return dfs(root.left, root.right)
        elif not root.left and not root.right:
            return True
        else:
            return False

# leetcode submit region end(Prohibit modification and deletion)
