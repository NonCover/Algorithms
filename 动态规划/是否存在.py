# @author: noc @time: 2020年1月5日
# 在一个整型数组中， 选择两两不相邻的若干个值， 是否让选择的值相加等于你所给定的值
# 动态规划
import numpy as np
'''
# 递归版
def  solution(arr, i, s):
    if s == 0:  # s = 0 时， 当前选择的值相加以及等于0，条件以及成立
        return True
    elif i == 0:    # 当低轨道数组的第一个值时， 只需要比较 s 和 arr[0] 是否相等
        return arr[0] == s
    elif arr[i] > s:    # 如果当前的值大于 s 的话，不需要考虑选择这个值，直接跳过
        return solution(arr, i - 1, s)
    else: 
        choose = solution(arr, i - 1, s - arr[i])   # 如果选择该值的话， s - arr[i] 用来进行与下一次的值的比较
        notchoose = solution(arr, i - 1, s)     # 如果不选择，直接跳过该值，s 不变
        return choose or notchoose
'''

# 非递归版
def solution(arr, S):
    subset = np.zeros((len(arr), S + 1), dtype=bool)
    subset[0, :] = False
    subset[:, 0] = True
    if arr[0] < S:
        subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S + 1):
            if arr[i] > S:
                subset[i, s] = subset[i - 1, s]
            else:
                choose = subset[i -1, s - arr[i]]
                notchoose = subset[i - 1, s]
                subset[i, s] = choose or notchoose
    r, c = subset.shape
    # print(r, c)
    return subset[r - 1, c - 1]

if __name__ == "__main__":
    arr = [26, 14, 11, 4, 5, 2, 3]
    # print(solution(arr, len(arr) - 1, 9))
    print(solution(arr, 26))