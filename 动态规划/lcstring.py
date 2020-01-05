# @author: noc @time: 2019年12月30日
# 最长公共子串
# 与最长公共子序列的唯一区别就在于 最长公共子串是一段连续的公共字串

def dp(s1, s2):
    arr = [ [0 for _ in range(len(s2))] for _ in range(len(s1))]
    res = 0 # 需要定义一个变量 每次来保存当前公共子串的最大长度
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 or j == 0 and s1[i] == s2[j]:
                arr[i][j] = 1
                res = arr[i][j]
            else:
                if s1[i] == s2[j]:
                    arr[i][j] = arr[i-1][j-1] + 1
                    res = max(res, arr[i][j])
    return res

if __name__ == "__main__":
    res = dp('fiwqffassh', 'foshsasdadd')
    print(res)