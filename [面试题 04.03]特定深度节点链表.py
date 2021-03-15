# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,2,3,4,5,null,7,8]
# 
#         1
#        /  \ 
#       2    3
#      / \    \ 
#     4   5    7
#    /
#   8
# 
# 输出：[[1],[2,3],[4,5,7],[8]]
#  
#  Related Topics 树 广度优先搜索 
#  👍 45 👎 0



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        tmp_next = []

        def bfs(now_node, deep):
            if len(ans) < deep:
                ans.append(ListNode(now_node.val))
                tmp_next.append(ans[-1])
            else:
                tmp_next[deep - 1].next = ListNode(now_node.val)
                tmp_next[deep - 1] = tmp_next[deep - 1].next

            if now_node.left:
                bfs(now_node.left, deep + 1)

            if now_node.right:
                bfs(now_node.right, deep + 1)

        bfs(tree, 1)
        return ans

