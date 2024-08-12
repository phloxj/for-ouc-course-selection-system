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


def MakeWeek(L_Zero):  # 输入一门课程的L，输出处理后带一周上课时间L0
    L0 = [
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False, False, False]
    ]
    n = int((len(L_Zero) - 2) / 3)
    for j in range(1, n + 1):
        for i in range(int(L_Zero[3 * j]) - 1, int(L_Zero[3 * j + 1])):
            L0[L_Zero[3 * j - 1] - 1][i] = True
    L_Zero = L_Zero[:2] + [L0]
    return L_Zero


def add_matrix(La, Lb):
    # 初始化结果列表
    result = []
    # 遍历两个列表的索引
    for i in range(len(La)):
        # 初始化当前子列表的结果
        subresult = []
        # 遍历子列表的索引
        for j in range(len(La[i])):
            # 使用逻辑或操作符来合并对应位置的元素
            subresult.append(La[i][j] or Lb[i][j])
            # 将当前子列表的结果添加到结果列表中
        result.append(subresult)
        # 返回合并后的列表
    return result


def custom_logic(a, b):
    if a and b:
        return False
    elif a and not b:
        return True
    elif not a and not b:
        return False
    else:  # 对应“F,T”的情况
        print("输入错误！")
        return None  # 或者你可以选择返回一个错误信息或特定的值


def subtract_matrix(La, Lb):
    # 初始化结果列表
    result = []
    # 遍历两个列表的索引
    for i in range(len(La)):
        # 初始化当前子列表的结果
        subresult = []
        # 遍历子列表的索引
        for j in range(len(La[i])):
            # 使用逻辑或操作符来合并对应位置的元素
            subresult.append(custom_logic(La[i][j], Lb[i][j]))
            # 将当前子列表的结果添加到结果列表中
        result.append(subresult)
        # 返回合并后的列表
    return result
