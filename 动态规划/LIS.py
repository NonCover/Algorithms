'''
最长上升子序列：给一个数组，例如：【10， 9， 2， 5， 3， 7， 101， 18】 最长上升子序列为【2， 3， 7， 18】 返回 4
这道题当然我们可以用动态规划来做：
首先我们先明确dp[i]的含义：它表示以nums[i]结尾的最长上升子序列的长度
那么我们定义了dp[i]，我们再来研究状态转移方程。对了在找状态转移方程之前，先要进行base case
由于每个nums[i]都至少有一个上升子序列，那就是它本身。所以我们初始化dp数组中每一个值为1。
我们把数据缩小来研究。我们现在来找[2, 5, 9, 3]的最长上升子序列的长度，假设我们已经得出dp的前三个的值 dp = [1, 2, 3, ?]
那么我们如何得出第四个的答案，我们来找前三个的数哪一个数是小于当前数 3, 当前这个数就是nums[0]，只有它是小于 3 的，所以当前
dp[3] = dp[0] + 1，就是当前的答案。当然这只是一个实例。
状态转移方程：dp[i] = max(dp[i], max(dp[0, i) + 1))
'''
def solution(nums):
    size = len(nums)
    dp = [1] * size
    for i in range(size):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[size - 1]

def solution2(nums):
    ans = 0
    top = [0] * len(nums)
    for num in nums:
        l, r = 0, ans
        while l < r:
            mid = (l + r) // 2
            if num > top[mid]: l = mid + 1
            else: r = mid
        if l == ans: ans += 1
        top[r] = num
    # print(top)
    return ans

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 6]
    print(solution2(nums))