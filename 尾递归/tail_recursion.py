import  sys
sys.setrecursionlimit(9999)

def add(maxnum, sum):
    if maxnum > 0:
        return add(maxnum - 1, sum + maxnum)
    return sum

if __name__ == '__main__':
    out = add(1000, 0)
    print(out)
