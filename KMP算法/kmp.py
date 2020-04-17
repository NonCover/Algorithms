class KMP:
    __pat = ""
    __dp = None     # dp[i][j] i 代表当前的状态，j代表txt对应要出现的字符 dp[i][j] 表示下一步的状态
    def __init__(self, pat):
        self.__pat = pat
        self.__buildState()

    def __buildState(self):
        '''
        构建状态需要明确几点：
        1. 当前的字符的状态
        2. 即将出现的字符的转移状态
        '''
        M = len(self.__pat)
        self.__dp = [[0] * 256 for _ in range(M)]
        self.__dp[0][ord(self.__pat[0])] = 1    # 只有初次遇到这个状态的时候，状态才会增加。遇到其他字符继续保存状态为0
        X = 0 # 影子状态，通俗来讲就是当前状态所对应的子重叠状态,影子状态与当前状态的有最大相同前缀
        # 构建状态转移
        for i in range(1, M):
            for j in range(256):
                # 当前字符等于预期出现的就将状态 加1。无论出现任何字符，我们都可以去找他的影子状态所对应的下一个状态
                self.__dp[i][j] = self.__dp[X][j]
            self.__dp[i][ord(self.__pat[i])] = i + 1
            X = self.__dp[X][ord(self.__pat[i])]

    def search(self, txt):
        M = len(self.__pat)
        N = len(txt)
        state = 0   # 状态
        for i in range(N):
            state = self.__dp[state][ord(txt[i])]    # 更新当前的状态
            if state == M: return i - M + 1 # 当前状态如果等于匹配的字符pat最后一个则代表以及找到这个字符，返回起始位置
        return -1

if __name__ == '__main__':
    kmp = KMP('AAAAB')
    out1 = kmp.search('AAAABAAAA')
    print(out1)
    out2 = kmp.search('AAAAAAAAB')
    print(out2)