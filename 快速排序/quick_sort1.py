# 双指针
def qs(arr, low, high):
    if (low > high):
        return
    else:
        i, j = low, high
        pviot = arr[low]
        while (i < j):
            while i < j and arr[j] > pviot:
                j -= 1
            while i < j and arr[i] <= pviot:
                i += 1
            # 交换 a[i] a[j]
            if i < j:
                swop = arr[i]
                arr[i] = arr[j]
                arr[j] = swop
        # 交换 a[i] a[low]
        print(arr)
        swop = arr[i]
        arr[i] = arr[low]
        arr[low] = swop
        qs(arr, low, i-1)
        qs(arr, i+1, high)


def s(arr):
    if len(arr) > 0:
        qs(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [1,3,2,6,4,8,6]
    print(arr)
    s(arr)
    print(arr)