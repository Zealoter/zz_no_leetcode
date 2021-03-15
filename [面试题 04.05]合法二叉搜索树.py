class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(now_node, upper, under):
            if now_node.left:
                if now_node.left.val < now_node.val and under < now_node.left.val:
                    if not dfs(now_node.left, now_node.val, under):
                        return False
                else:
                    return False

            if now_node.right:
                if now_node.right.val > now_node.val and upper > now_node.right.val:
                    if not dfs(now_node.right, upper, now_node.val):
                        return False
                else:
                    return False
            return True

        return dfs(root, 99999999999, -99999999999)
