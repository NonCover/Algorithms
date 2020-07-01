"""
author: noc
time: 2020年7月1日
"""

"""
子集背包问题
leetcode: 416 问题描述
"""

def canPartition(arr: list):
    sm = 0
    for a in arr:
        sm += a
    if sm % 2 == 1:
        return False
    n = len(arr)
    sm //= 2
    # f = [[False] * (sm + 1) for _ in range(n + 1)]    # f[i][j] 代表前 i 个物品是否可以组成和为 j
    # for i in range(0, n + 1):
    #     f[i][0] = True        # base case
    # for i in range(1, n + 1):
    #     for j in range(1, sm + 1):
    #         if j - arr[i - 1] < 0:
    #             f[i][j] = f[i - 1][j]
    #         else:
    #             f[i][j] = f[i - 1][j] or f[i - 1][j - arr[i - 1]]
    """
    状压DP， 由于每次状态只与上一次有关
    """
    f = [False] * (sm + 1)
    f[0] = True
    for k in range(n):
        for i in range(sm, -1, -1):
            if i - arr[k] >= 0:
                f[i] = f[i] or f[i - arr[k]]
    return f[-1]

if __name__ == '__main__':
    a = [2, 4, 4, 6, 2]
    out = canPartition(a)
    print(out)