'''
@author: noc
@time: 2020年3月8日

完全背包问题：
    有N个物品和一个容量为V的背包，每个物品都可以无限的使用
    第i个物品的体积为Vi， 价值为 Wi
    怎样装，才能让背包的总价值最大
'''
n, m = 4, 5     # 4个物品，容量为5
f = [0] * (m + 1)
v = [0, 1, 2, 2, 4]     # 体积
w = [0, 2, 6, 2, 1]     # 价值

if __name__ == "__main__":
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j >= v[i]:
                f[j] = max(f[j], f[j - v[i]] + w[i])
        print(f)
    print(f[m])