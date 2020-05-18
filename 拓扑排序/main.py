"""
拓扑排序：言简意赅就是对一个有向无环的图进行排序，排序规则是按照图的方向进行排序。
我会介绍两种方法，dfs和bfs
"""
"""
构建一个有向无环图，我们用Python的集合类来构造
"""
import  collections
edeges = collections.defaultdict(list)
edeges[1] = [2, 4]
edeges[2] = [3]
edeges[4] = [3]
# edeges[3] = [4]
nums = 4    ## 节点个数
"""
DFS解法
"""
def topo_sort1():
    ## 一个数组来保存一个节点是否访问过，0 = 为访问 1 = 访问过 2 = 访问完毕
    seen = [0] * (nums + 1)
    res = []    ## 存放拓扑排序结果
    ## 递归实现（栈空间）
    def dfs(i):
        ## 访问过，说明有环
        if seen[i] == 1:
            return False
        ## 访问完毕，直接返回
        if seen[i] == 2:
            return True
        ## 没有访问，设为访问
        seen[i] = 1
        ## 将当前节点加入到栈中，相当于调用dfs
        for e in edeges[i]:
            if not dfs(e):
                return False
        ## 访问完毕
        seen[i] = 2
        ## 加入到答案数组中去
        res.append(i)
        return True

    for i in range(1, nums + 1):
        if not dfs(i):
            """如果存在环就无法进行拓扑排序"""
            return []
    ## 结果需要取反，因为栈满足的是先进后出
    return res[::-1]

"""
BFS解法
"""
def topo_sort2():
    ## 存放的是每个节点的入度
    in_degree = [0] * (nums + 1)
    for i in range(1, nums + 1):
        for j in edeges[i]:
            in_degree[j] += 1
    ## 队列实现BFS，把入度为0加进去
    queue = collections.deque([i for i in range(1, nums) if in_degree[i] == 0])
    res = []    ## 存放结果
    while queue:
        curr = queue.popleft()
        res.append(curr)
        for i in edeges[curr]:
            ## 当前节点指向的所有的节点的入度减一
            in_degree[i] -= 1
            if in_degree[i] == 0: queue.append(i)
    ## 如果结果数组的长度不等于需要存放的长度，则说明图存在环
    return res if len(res) == nums else []

if __name__ == '__main__':
    o = topo_sort1()
    print(o)