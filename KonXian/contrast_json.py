import json


def is_clash(La, Lb):
    # 遍历两个二维列表的索引
    for i in range(len(La)):
        # 遍历子列表的索引
        for j in range(len(La[i])):
            # 检查是否都包含值为True的元素
            if La[i][j] and Lb[i][j]:  # 使用逻辑与操作符来检查两个布尔值
                return True  # 找到匹配的元素，返回True
    # 没有找到匹配的元素
    return False


def get_clash_json():
    with open('./data/output.json', 'r') as f:
        # 使用json.load()读取文件内容并解码成Python对象
        output = json.load(f)
    with open('./data/xuan.json', 'r') as f:
        # 使用json.load()读取文件内容并解码成Python对象
        xuan = json.load(f)

    not_clash = []
    for xuan_i in xuan:
        if not is_clash(output, xuan_i[2]):
            not_clash += [xuan_i[0]]

    with open('./data/not_clash.json', 'w') as f:
        # 使用json.dump()方法将列表写入文件
        json.dump(not_clash, f, indent=4)  # indent=4用于美化输出，使JSON文件更易读
