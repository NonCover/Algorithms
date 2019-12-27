# @author: noc @time: 2019年12月27日
# 集合覆盖问题
# 如果你要开办一个广播台， 且每个广播站所覆盖的信号省份不一样， 如何使用
# 最少的广播站来完成广播台的播放

# 需要播放的省份
province = set(['四川', '重庆', '贵州', '福建', '云南', '广西', '宁夏', '湖南', '湖北'])

# 每个广播站所覆盖的面积
stand_cover = {
    'one': set(['四川', '重庆', '贵州']),
    'two': set(['重庆', '云南', '贵州']),
    'three': set(['四川', '重庆']),
    'four': set(['湖南', '湖北', '广西']),
    'five': set(['福建', '宁夏', '湖北'])
}

def find_Least_stand(province):
    # 存放需要的广播站
    needed_stand = set()
    while province:
        stand = None    # 记录覆盖最多未被覆盖的广播站
        stand_covered = set()   # 记录覆盖过的省份
        for stand_name, stand_cover_province in stand_cover.items():
            stand_in = province & stand_cover_province      # 交际运算， 获取覆盖最多未被覆盖的广播站
            if len(stand_in) > len(stand_covered):  # 当前包含的省份比上一个的多
                stand = stand_name      # 更新
                stand_covered = stand_in    # 更新
        needed_stand.add(stand)     # 更新需要的广播站
        province -= stand_covered   # 从总集合中删除包含过的元素

    return needed_stand

if __name__ == "__main__":
    print(find_Least_stand(province))