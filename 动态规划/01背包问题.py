N = 1024
n, m = 4, 5         # 有4个物品，背包容量为5
# f = [[0] * (m+1)] * (n+1)
# 优化成一维数组
f = [0] * (m + 1)
v = [0, 1, 2, 2, 4]     # 体积
w = [0, 2, 4, 4, 5]     # 价值
if __name__ == "__main__":
    for i in range(1, n+1):
        for j in range(m, 0, -1):
            if j >= v[i]:   # 当前物品装得下
                f[j] = max(f[j], f[j - v[i]] + w[i]) # 当前物品的体积能够装的下，就加上前i个物品的最佳组合，在比较不装当前物品的最佳选择
        print(f, end=" , ")
    print(f[m])  # 打印的最后结果