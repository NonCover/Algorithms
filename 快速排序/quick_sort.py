# @author: noc @time: 2019年12月22日

# 快速排序
def quicksort(arr):
    if len(arr) < 2:
        # 当数组长度为 0 和 1 时， 直接返回数组
        return arr
    else: 
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]   # 所有小于等于pivot的值 组成一个数组
        greater = [i for i in arr[1:] if i > pivot] # 所有大于pivot的值 组成一个子数组
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    print(quicksort([2,5,1,5,3]))