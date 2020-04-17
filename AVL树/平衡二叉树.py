'''
@author:noc
@time;2020年4月10日
'''

class Tree:
    def __init__(self, x):
        self.val = x
        self.lchid = None
        self.rchid = None
        self.bf = 0 # 平衡因子

class AVL:
    def __init__(self):
        self.root = None
    

if __name__ == '__main__':
    arr = [23, 21, 34, 32, 16, 27, 14]
