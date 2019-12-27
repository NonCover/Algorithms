import math
graph = {
    'A':{'B':5, 'C':1},
    'B':{'D':1},
    'C':{'D':4, 'E':8},
    'D':{'F':6},
    'E':{},
    'F':{}
}

def init_costs(start):
    '''对每个节点所需要的路程进行初始化'''
    costs = {start:0}
    for v in graph:
        if v != start:
            costs[v] = math.inf     # 初始化的节点路程为无穷大
    return costs

def find_lowest_node(costs, visted):
    lowest_cost = math.inf  # 记录最低开销
    lowest_cost_node = None # 记录最低开销的节点
    for node in costs:
        cost = costs[node]  # 当前节点的开销
        if cost < lowest_cost and node not in visted:   # 当前节点开销更低，且未被处理过
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def find_lowest_path(start, end):
    parents = {start:None}  # 存放父节点
    visted = set()
    costs = init_costs(start)   # 初始化各节点的路程
    node = find_lowest_node(costs, visted)
    while node is not None:     # 节点不为空
        cost = costs[node]
        neighbors = graph[node] # 当前节点附近的节点
        for n in neighbors.keys():
            new_cost = cost + neighbors[n] # 记录节点的新开销
            if new_cost < costs[n]:
                costs[n] = new_cost        # 更新节点的开销
                parents[n] = node          # 更新节点的父节点
            if n == end:    # 当前节点为要寻找的节点
                    return costs[end], parents
        visted.add(node)
        node = find_lowest_node(costs, visted)  # 再去找最低开销的节点
    # return costs

if __name__ == "__main__":
     print(find_lowest_path('A', 'E'))
