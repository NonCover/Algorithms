"""
author：noc
time：2020年6月8日
并查集的实现
"""
"""
用于判断一个无向图中是否存在环
"""

## 元组代表 每两个点相连
## edegs 6个节点，6条边
edegs = [
    (0, 1), (1, 3), (1, 2),
    (3, 5), (2, 4), (3, 4)
]

## 如果图退化成链表的话，我们每次查找需要耗费大量时间。所以我们按轶合并两个节点

def union(x, y, parent, depth):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)
    if x_root == y_root: return 0   ## 代表两个节点的根节点一样，在同一个树中
    else:
        if depth[x_root] > depth[y_root]:
            parent[y_root] = x_root
        elif depth[x_root] < depth[y_root]:
            parent[x_root] = y_root
        else:
            ## 相等情况的话，无论那个节点作为根节点都可以，只是作为根节点的深度需要加1
            parent[y_root] = x_root
            depth[x_root] += 1
        return 1

def find_root(x, parent):
    ## 找到当前节点的根节点
    root = x
    ## 相当于找到值为 -1 的下标
    while (parent[root] != -1):
        root = parent[root]
    return root

if __name__ == '__main__':
    parent = [-1] * 6       ## parent[i] = j    i 的父节点为 j, 为 -1 的话，代表为根节点
    depth = [0] * 6         ## 每个节点的树的深度
    ## 判断图是否存在环
    for i in range(6):
        x, y = edegs[i]
        if (union(x, y, parent, depth) == 0):
            print("有环")
            # print(parent)
            break
    else: print("没有环")