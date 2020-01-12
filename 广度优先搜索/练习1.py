'''
    @author: noc
    @time: 2020年1月12日
    @url: https://www.bilibili.com/video/av9922119
'''
def rc(rectangle):
    res = rectangle[::-1]
    return res

def rmc(rectangle):
    res = rectangle[3] + rectangle[0:3] + rectangle[-3:] + rectangle[4] 
    return res

def rrc(rectangle):
    res = rectangle[0] + rectangle[-2] + rectangle[1] + rectangle[3:5] + rectangle[2] + rectangle[-3] + rectangle[-1]
    return res

def change(rectangle, i):
    if i == 0:
        return rc(rectangle)
    if i == 1:
        return rmc(rectangle)
    else:
        return rrc(rectangle)

def course(parents, node):
    print("Course:")
    while node:
        print(node, end=" <- ")
        node = parents[node]
    print("Begin")

def bfs(rectangle):
    parents = {rectangle: None} # 存放每个节点的父节点
    solution = input("Solution: ")
    queue = [rectangle] # 队列
    visted = set() # 集合，存放检查过的节点
    visted.add(rectangle)
    while queue != None:    # 队列为空运行完毕
        node  = queue.pop(0)    # 出队
        if node == solution:
            print("Solution is found...")
            course(parents, node)
            break
        else:
            for i in range(3):
                child = change(node, i)
                if child not in visted:
                    visted.add(child)
                    queue.append(child)
                    parents[child] = node

if __name__ == "__main__":
    bfs("12345678")