# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。 
# 
#  示例1: 
# 
#   输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
#  
# 
#  示例2: 
# 
#   输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [
# 1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出 true
#  
# 
#  提示： 
# 
#  
#  节点数量n在[0, 1e5]范围内。 
#  节点编号大于等于 0 小于 n。 
#  图中可能存在自环和平行边。 
#  
#  Related Topics 图 
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        tmp_map=[[] for i in range(n)]
        for tmp_line in graph:
            tmp_map[tmp_line[0]].append(tmp_line)

        flag=[0]*n

        def dfs(now):
            if flag[now]==1:
                return False
            if now==target:
                return True
            flag[now]=1
            for next_point in tmp_map[now]:
                if dfs(next_point[1]):
                    return True
        if dfs(start):
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
