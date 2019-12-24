import random
# 双指针
def qs(arr, low, high):
    # print(arr[low:high+1])
    if (low > high):
        return
    else:
        i, j = low, high
        # 随机选取基准值
        rand = random.randint(low, high)  # 数组的随机下标
        pviot = arr[rand]
        # 基值 与 最右边的值交换
        swop = arr[high]
        arr[high] = arr[rand]
        arr[rand] = swop
        while (i < j):
            while i < j and arr[i] < pviot:
                i += 1
            while i < j and arr[j] >= pviot:
                j -= 1
            # 交换 a[i] a[j]
            if i < j:
                swop = arr[i]
                arr[i] = arr[j]
                arr[j] = swop
        # 交换 a[i] pviot
        swop = arr[j]
        arr[j] = arr[high]
        arr[high] = swop
        qs(arr, low, i-1)
        qs(arr, i+1, high)

def s(arr):
    if len(arr) > 0:
        qs(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    # arr = [3, 2, 5, 4, -1, 3, 41, 5, 12, 3, 7]
    # arr = [1,0]
    arr = []
    print(arr)
    s(arr)
    print(arr)