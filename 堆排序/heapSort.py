# @author: noc
# @time：2020年1月17日
# @url：https://www.bilibili.com/video/av47196993   参考教程
 
def swap(arr, i, j):
     # 交换数组中两个值
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapify(arr, n, i):
    """
    构建堆得过程
    """
    if i >= n: return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    mx = i
    if c1 < n and arr[c1] > arr[mx]:
        mx = c1
    if c2 < n and arr[c2] > arr[mx]:
        mx = c2
    if mx !=  i:
        swap(arr, mx, i)
        heapify(arr, n, mx)

def heap_sort(arr, n):
    """
    每次heapify后，将堆顶元素与最后一个交换，下次计算就不用计算最后一个，每次长度减 1
    """
    build_heap(arr, n)
    for i in range(n - 1, -1, -1):
        swap(arr, i, 0)         ## 堆顶拿出来
        build_heap(arr, i)

def build_heap(arr, n):
    """
    从非叶子节点开始，从下到上，从右到左依次构建堆
    """
    last = n - 1
    parent = (last - 1) // 2
    for i in range(parent, -1, -1):
        heapify(arr, n, i)


if __name__ == "__main__":
    # 完整二叉树:
    arr = [6, 7, 4, 8, 1, 10, 5]
    n = len(arr)
    heap_sort(arr, n)
    print(arr)