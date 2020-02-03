'''
@author: noc
@time: 2020年2月3日
@url: https://blog.csdn.net/qq_26399665/article/details/79831490 参考链接
'''

# -*- coding:utf-8 -*-

import random

def swap(arr, i, j):
    '''
    交换两个值
    '''
    arr[i], arr[j] = arr[j], arr[i]

def kd(arr):
    '''
    算法时间复杂度 O（n）
    属于原地打乱顺序的一种，不需要额外开辟存储打乱后的数组的空间
    '''
    i = len(arr)
    for i in range(i - 1, -1, -1):
        swap(arr, i, random.randint(0, i))
    return arr

if __name__ == "__main__":
    arr = [2, 3, 1, 4]
    print(kd(arr))