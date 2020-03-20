
'''
牛顿迭代法求平方根
'''

def f(r, n):
    return r**2 - n

def _f(r):
    return r*r

def newton_iteration(n):
    r = n
    while f(r, n) > 0.000000001 or _f(r) < -0.000000001:
        r = (r + n / r) / 2
        # r = r - (f(r, n) / _f(r))
    return r

if __name__ == '__main__':
    print(newton_iteration(9))
