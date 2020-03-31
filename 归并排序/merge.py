'''
归并排序
'''

def merge_sort(arr):
    mid = len(arr) // 2
    # 递归出口，当数组的长度分到只有一个或零个，直接返回该数组
    if mid == 0:
        return arr
    # 不断 分
    left = arr[:mid]
    right = arr[mid:]
    # 合并两个数组并排序，治。
    return _merge(merge_sort(left), merge_sort(right))

def _merge(left, right):
    ret = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            ret.append(right.pop(0))
        else:
            ret.append(left.pop(0))
    ret += left
    ret += right
    return ret

if __name__ == '__main__':
    array = [5, 4, 7, 6, 3, 1, 2, 8]
    # 升序排序
    print(merge_sort(array))
