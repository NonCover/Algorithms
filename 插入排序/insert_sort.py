'''
与冒泡排序有一点相似。
时间复杂度都是 O（n*n） 只是在最好情况下插入排序是O（nlogn），其实所谓的最好情况，也就是排序数组五五开是排好序的。比如 【1，3，5，6，2，4，8】
'''
def sort(arr):
    if len(arr) <= 1: return
    for i in range(1, len(arr)):
        j, v = i, arr[i]
        # 找到一个首个比v小的数，将v插入到这个数之后即可，后面的数依次向后移动一个
        while arr[j - 1] > v and j > 0:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = v

if __name__ == '__main__':
    arr = [2, 1, 4, 5, 2, 6, 5]
    sort(arr)
    print(arr)