def minWindow(s, t):
    left, right = 0, 0
    start, minLen = 0, 0x7fffffff
    needs, window = dict(), dict()
    for c in t:
        if c not in needs:
            needs[c], window[c] = 1, 0
        else: needs[c] += 1
    match = 0       # 统计s中出现t中字符的个数
    while right < len(s):
        c1 = s[right]
        if (c1 in needs.keys()):
            window[c1] += 1
            ## 当窗口内出现某个字符的个数满足需要出现的个数的话
            if window[c1] == needs[c1]: match += 1
        while match == len(t):
            ## 更新窗口，使其满足最小长度
            if (right - left < minLen):
                start = left
                minLen = right - left
            c2 = s[left]
            if (c2 in needs.keys()):
                window[c2] -= 1
                ## 当这个字符出现的次数不满足条件，继续滑窗，right继续向前寻找
                if (window[c2] < needs[c2]):
                    match -= 1
            left += 1
        right += 1

    return s[start:start + minLen+1] if minLen != 0x7fffffff else ""

if __name__ == '__main__':
    s = "DFSEGANCD"
    v = "DE"
    print(minWindow(s, v))