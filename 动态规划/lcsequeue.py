# @author: noc  @time: 2019年12月29日
# 利用动态规划计算两个单词的最长公共字序列
# 例如：fosh fish 
#  f o s h
#  f i s h
#  √ × √ √


def dp(word1, word2):
    # 创建一个 行为 word1， 列为 word2 的二维数组
    arr = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
    '''
        arr如下所示 
              f o s h
            f 0 0 0 0
            i 0 0 0 0
            s 0 0 0 0
            h 0 0 0 0 <- 这个值就是最后的答案 也就是最长公共子序列的长度
    '''
    for i_index, i_elem in enumerate(word2):
        for j_index, j_elem in enumerate(word1):
            # arr[0][0] 需要单独判断，防止超出数组长度
            if i_index == 0 and j_index == 0:
                if i_elem == j_elem:
                    arr[i_index][i_index] = 1
            # arr[0][j_index] 单独处理
            elif i_index == 0:
                if i_elem == j_elem:
                    arr[i_index][j_index] = arr[i_index][j_index - 1] + 1
                else:
                    arr[i_index][j_index] = arr[i_index][j_index - 1]
            # arr[i_index][0] 单独处理
            elif j_index == 0:
                if i_elem == j_elem:
                    arr[i_index][j_index] = arr[i_index - 1][j_index] + 1
                else:
                    arr[i_index][j_index] = arr[i_index - 1][j_index]
            # 正常处理
            else:
                if i_elem == j_elem:
                    arr[i_index][j_index] = arr[i_index - 1][j_index - 1] + 1
                else:
                    arr[i_index][j_index] = max(arr[i_index - 1][j_index], arr[i_index][j_index - 1])
    return arr

if __name__ == "__main__":
    res = dp('ffff', 'ffff')
    for i in res:
        print(i)
        '''
        [1, 2, 3, 4]
        [2, 2, 3, 4]
        [3, 3, 3, 4]
        [4, 4, 4, 4]
        '''