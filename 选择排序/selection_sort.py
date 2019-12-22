# @author：noc @time：2019年12月19日
# 选择排序

def findSmallest(arr):
    '''
    :param arr: 数组
    :return: 最小值下标
    '''
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return  smallest_index

def solution(arr):
    '''
    :param arr: 数组
    :return: 排序后的数组
    '''
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))   # 删除arr的最小值并将该值加入到新数组
    return newArr

if __name__ == '__main__':
    print(solution([2,5,1,6,3,9]))