# 设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#      3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。 
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。 
# 
#  说明: 
# 
#  所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。 
#  Related Topics 树 
#  👍 32 👎 0


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def fun(tmp_node):
            tmp_ans = 0

            if tmp_node.val == p.val or tmp_node.val == q.val:
                tmp_ans += 1

            if tmp_node.left:
                num = fun(tmp_node.left)
                if num == 1:
                    tmp_ans += 1
                elif num == 0:
                    pass
                else:
                    return num
            if tmp_node.right:
                num = fun(tmp_node.right)
                if num == 1:
                    tmp_ans += 1
                elif num == 0:
                    pass
                else:
                    return num
            if tmp_ans == 2:
                return tmp_node
            else:
                return tmp_ans

        ans = fun(root)
        return ans
