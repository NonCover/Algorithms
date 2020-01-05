# @author: noc @time: 2020年1月5日
# 给定一个整型数组，选择数组中不两两相邻的一些值，如何选择能使值最大
# 动态规划求解
# 例如: [1, 4, 4, 5, 7, 9]  max = 18    [4, 5, 9]
# 非递归法
# import numpy as np
# 公式:
#           | 不选该值: np[i-1}    
#   np[i] = |
#           | 选择: np[i - 2] + np[i]

def solution(arr):
    np = [ 0 for _ in range(len(arr))]  # 该数组用来保存每一步的最大值
    np[0] = arr[0]
    np[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        choose = arr[i] + np[i - 2]
        notchoose = np[i - 1]
        np[i] = max(choose, notchoose)  # 更新当前选择的最大值
    return np

def main():
    arr = [1, 4, 4, 5, 7, 9]
    res = solution(arr)
    print(res)  # 数组的最后一个值 则为正确答案

if __name__ == "__main__":
    main()

