'''
总结思路：
滑动窗口无非就是左右两个指针，右指针先移动，当移动到某个位置时，不满足条件后，就开始移动左指针，直到又再一次满足条件，又移动右指针。往往复复
当然，我们在移动的时候还得要更新答案。具体根据题目定
'''
def lengthOfLongestSubstring(s):
    left, right = 0, 0
    ans = float('-inf')
    window = dict()
    while right < len(s):
        ## 没有重复出现加入道其中计数
        if s[right] not in window:
            window[s[right]] = 1
        else: window[s[right]] += 1
        ## 重复出现开始移动left
        while window[s[right]] > 1:
            window[s[left]] -= 1
            left += 1
        right += 1
        ans = max(ans, right - left)
    return ans
if __name__ == '__main__':
    s = "abcbacdes"
    print(lengthOfLongestSubstring(s))