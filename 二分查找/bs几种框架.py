'''零 二分查找框架'''
'''
def bs1(nums, target):
    left, right = 0, ...
    while (...):
        ## 此方法是防止溢出，在Python中不会考虑此问题
        mid = left + (right - left) // 2
        ## mid = (left + right) // 2
        if (target == nums[mid]):
            pass
        elif (target < nums[mid]):
            right = ...
        elif (target > nums[mid]):
            left = ...
    return ...
'''
'''基本用法1：寻找一个数'''
def bs1(nums, target):
    left, right = 0, len(nums) - 1
    while (left <= right):
        ## 此方法是防止溢出，在Python中不会考虑此问题
        mid = left + (right - left) // 2
        ## mid = (left + right) // 2
        if (target == nums[mid]):
            return mid
        elif (target < nums[mid]):
            right = mid - 1
        elif (target > nums[mid]):
            left = mid + 1
    return -1
'''基本用法2：寻找左侧边界的一个数'''
def bs2(nums, target):
    ## 搜索区间 [left, right]
    left, right = 0, len(nums) - 1
    while (left <= right):       # 注意
        ## 此方法是防止溢出，在Python中不会考虑此问题
        mid = left + (right - left) // 2
        if (target == nums[mid]):
            ## 缩小搜索区间 [left, mid - 1]
            right = mid - 1     # 注意
        elif (target < nums[mid]):
            ## 搜索区间[left, mid - 1]
            right = mid - 1     # 注意
        elif (target > nums[mid]):
            ## 搜索区间[mid + 1, right]
            left = mid + 1
    ## 防止出界
    if (left >= len(nums) or nums[left] != target): return -1
    return left

'''基本用法3：寻找右侧边界的一个数'''
def bs3(nums, target):
    left, right = 0, len(nums) - 1
    print(left, right)
    while left <= right:
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        if (nums[mid] == target):
            left = mid + 1
        elif (nums[mid] < target):
            left = mid + 1
        elif (nums[mid] > target):
            right = mid - 1
        print(left, right)
    if (right < 0 or nums[right] != target): return -1
    return right

class BS:
    '''
    由于几种方法都有很多种写法，我将最终写法写在此。我们统一采用左闭右开的形式
    '''
    def binary_search(self, nums, target):
        return self.__binary_search(nums, target)

    def left_bound(self, nums, target):
        return self.__left_boud(nums, target)

    def right_bound(self, nums, target):
        return self.__right_bound(nums, target)

    def __binary_search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                right = mid
            elif (target > nums[mid]):
                left = mid + 1
        return -1

    def __left_boud(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if (target == nums[mid]):
                right = mid
            elif (target < nums[mid]):
                right = mid
            elif (target > nums[mid]):
                left = mid + 1
        ## 由于最后left或者right可能出界
        if (left >= len(nums) or nums[left] != target): return -1
        ## 同 return right
        return left

    def __right_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                left = mid + 1
            elif (target < nums[mid]):
                right = mid
            elif (target > nums[mid]):
                left = mid + 1
        ## 因为 left = mid + 1这一步的关系，left实际在的位置会在答案后一位，需要减一
        if (left - 1 < 0 or nums[left - 1] != target): return -1
        ## 同 return left - 1
        return right - 1


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3]
    print(BS().binary_search(nums, 12))
    print(BS().left_bound(nums, 2))
    print(BS().right_bound(nums, 2))