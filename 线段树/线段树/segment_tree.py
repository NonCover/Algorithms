'''
@author：noc
@time：2020年1月27日
@url：https://www.bilibili.com/video/av47331849
'''

def build_tree(arr, tree, node, start, end):
    # 参考树状数组
    # 构造线段树:
    if start == end:
        tree[node] = arr[start]
    else:
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        mid = (start + end) // 2
        build_tree(arr, tree, left_node, start, mid)
        build_tree(arr, tree, right_node, mid + 1, end)
        tree[node] = tree[left_node] + tree[right_node]

def update_tree(arr, tree, node, start, end, idx, val):
    # 更新线段树
    if start == end:
        arr[idx] = val
        tree[node] = val
        return
    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    if (idx >= start and idx <= mid):   # 当idx出现在arr的 start - end 范围内
        update_tree(arr, tree, left_node, start, mid, idx, val)
    else:
        update_tree(arr, tree, right_node, mid + 1, end, idx, val)
    tree[node] = tree[left_node] + tree[right_node]        

def query_tree(arr, tree, node, start, end, L, R):
    # 计算
    if (R < start or L > end):
        return 0
    elif (start == end):
        return tree[node]
    mid = (start + end) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2
    left_sum = query_tree(arr, tree, left_node, start, mid, L, R)
    right_sum = query_tree(arr, tree, right_node, mid + 1, end, L, R)
    return left_sum + right_sum

def main():
    arr = [1, 3, 5, 7, 9]
    tree = [None for _ in range(9)]
    build_tree(arr, tree, 0, 0, 4)
    print(tree)
    update_tree(arr, tree, 0, 0, 4, 3, 6)
    print(tree)
    print(query_tree(arr, tree, 0, 0, 4, 1, 3))

if __name__ == "__main__":
    main()