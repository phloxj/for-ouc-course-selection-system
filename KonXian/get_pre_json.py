import os
import openpyxl
import json


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
            if i <= 11:
                L0[L_Zero[3 * j - 1] - 1][i] = True
            else:
                print('错误：', L_Zero)  # 点名批评黄鹏老师，您上哪来的(13-14节)?
    L_Zero = L_Zero[:2] + [L0]
    return L_Zero


def get_json(file_path):
    # 定位preprocess
    folder_path, file_name = os.path.split(file_path)
    file_name = 'preprocess' + file_name[-10:]
    file_path = folder_path + '/' + file_name

    xuan = []
    workbook = openpyxl.load_workbook(file_path)
    kcfw = ['Specialty', 'Common', 'PublicBasic']  # 课程范围
    for kc in kcfw:
        sheet_name = kc
        sheet = workbook[sheet_name]
        column_values = [cell.value for cell in sheet['B']]
        jishu = 1
        for value in column_values:
            if value is not None:
                xuan += [[cell.value for cell in sheet[jishu]]]
            else:
                L = [cell.value for cell in sheet[jishu]]
                del L[0]
                del L[0]
                xuan[len(xuan) - 1] += L
            jishu += 1

    # print(bi)
    # print(xuan)

    L_New = []

    for lst in xuan:
        L_New += [MakeWeek(lst)]
    # 打开（或创建）一个文件用于写入
    with open('./data/xuan.json', 'w') as f:
        # 使用json.dump()方法将列表写入文件
        json.dump(L_New, f, indent=4)  # indent=4用于美化输出，使JSON文件更易读
