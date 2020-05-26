"""
floyd algorithm
"""
MAX_VALUE = float('inf')

path = [[0, 2, 6, 4],
        [MAX_VALUE, 0, 3, MAX_VALUE],
        [7, MAX_VALUE, 0, 1],
        [5, MAX_VALUE, 12, 0]]

## path[i][j] 代表从i -> j的所需的路程(下标表示节点)
## path[i][j] = MAX_VALUE 代表从i -> j走不通
## path[i][j] = 0 表示 i = j，意味着从i 走向 i路程为0


"""
佛洛依德算法本质上就是动态规划。
例如 我们从0 -> 1 的路程为 5， 0 -> 2 = 2， 2 -> 1 = 1,
那么我们肯定走 0 -> 2 -> 1这样的路程，同时我们将更新 0 -> 1的路程为 1, 这里就是我们的任意两个节点的最短路成的子状态，
我们用path[i][j]来保存这样的子状态, 其实这个算法比起迪杰斯特拉算法更好理解，也更简单，只需要三个循环就能解决任意两个节点的
最短路径。
基本思想如下：
我们有 n 个节点，编号从 0 ~ n，我们先更新 i 通过 0 到达 j 的最短路成，如果 i 到 j 的路程小于 通过 0 到达的路程，那么就不用更新，反之。
然后依次更新 i 通过 1....n 到 j 的最短路程。
"""

if __name__ == '__main__':
    ## floyd算法，运用动态规划的思想
    ## 初始
    print("初始路程：")
    for i in path:
        print(i)
    width, height = 4, 4
    for v in range(height):     ## 所有中转节点
        for i in range(height):
            for j in range(width):
                """
                这一步相当于状态转移方程，path[i][v] + path[v][j] = i -> v -> j的路程
                更新i -> j的最短路程
                """
                path[i][j] = min(path[i][j], path[i][v] + path[v][j])

    print("计算最短路程后:")
    for i in path:
        print(i)
