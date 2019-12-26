# @author: noc @time：2019年12月26日
# 创建图
graph = {}
graph['me'] = ['bob', 'jack']
graph['jack'] = ['alice']
graph['bob'] = ['alice', 'tom']
graph['alice'] = ['tom']
graph['tom'] = ['jonh']

def search(start, name):
    visted = set()  # 存放检查过的人
    queue = []  # 创建的队列
    queue.append(start)
    while queue:
        # print(queue)
        person = queue.pop(0)   # 出队
        if person != name:
            visted.add(person)  # 不是这个人的话加入到检查过的人中
            queue += graph[person] # 将这个人认识的人加入到队列中查找
        else:
            return True
    return False

if __name__ == "__main__":
    print(search('me', 'tom'))