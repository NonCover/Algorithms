# @author: noc
# @time：2020年1月17日
# @url：https://www.bilibili.com/video/av47196993   参考教程
 
def swap(arrs, i, j):
     # 交换数组中两个值
    stemp = arrs[i]
    arrs[i] = arrs[j]
    arrs[j] = stemp

# 创建大顶堆 
def heapify(arrs, i, length):
    if i > length:
        return
    leftChild = 2 * i + 1   # 左子节点
    rightChild = 2 * i + 2  # 右子节点
    maxNode = i
    if leftChild <= length:
        if arrs[leftChild] > arrs[maxNode]:
            maxNode = leftChild   # 最大节点等于左子节点
    if rightChild <= length:
        if arrs[rightChild] > arrs[maxNode]:
            maxNode = rightChild  # 最大节点等于右子节点
    if arrs[maxNode] != arrs[i]:    
        swap(arrs, i, maxNode)  # 交换父节点和 最大值
        heapify(arrs, maxNode, length)

def build_heap(arrs, length):
    for i in range( (length - 1) // 2 , -1, -1):
        # print(arrs)
        heapify(arrs, i, length - 1)
    swap(arrs, 0, length - 1)

def heapsort(arrs):
    for i in range( len(arrs), 2, -1 ):
        build_heap(arrs, i)
        # print(arrs, i)

def main(arr):
    heapsort(arr)    
    print(arr)

if __name__ == "__main__":
    # 完整二叉树:
    main([4, 2, 6, 8, 3, 10, 1, 0, 7, 5])