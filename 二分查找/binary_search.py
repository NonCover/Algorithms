# @author: noc
# @time: 2019年12月18日
# @what to do:
# 二分查找

def solution(nums, item):
    '''
    :param nums: 有序数组
    :param item: 查找的元素
    :return: 元素所在位置的索引，没有返回None
    '''
    # 定义两个指针来操作数组
    low = 0
    high = len(nums) - 1
    while low <= high:
        # 当low > high时， 整个数组全部遍历完，则返回None
        mid = (low + high) // 2   # 取两个指针所指向的数组段的中间下表，自动取整 例：5 // 2 = 2
        guess = nums[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1   # guess 小于item， low移动到mid+1的位置
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    nums = [1,4,5,6,7,9,12,13,15,14]
    item = 20
    res = solution(nums, item)
    print(res)