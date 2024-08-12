import openpyxl
import json
from fanction import MakeWeek

# 输入数据
bixuan = [
    '高等数学Ⅰ2',
    '热学',
    '电磁学',
    '模拟电子技术',
    '物理学实验1',
    '创新与学术实训',
    'MATLAB程序设计与应用',
    '军事科学概论',
    '形势与政策-2024春',
    '中国近现代史纲要',
    '大学英语Ⅱ',
]
file_path = r"C:\Users\qwe_r\Documents\选课\preprocess20231.xlsx"  # 打开路径


def lst(ji):
    return [cell.value for cell in sheet[ji]]


bi = []
xuan = []
workbook = openpyxl.load_workbook(file_path)
kcfw = ['Specialty', 'Common', 'PublicBasic']  # 课程范围
for kc in kcfw:
    sheet_name = kc
    sheet = workbook[sheet_name]
    column_values = [cell.value for cell in sheet['B']]
    jishu = 1
    val = '0'
    for value in column_values:
        if value is not None:
            val = value
            if value in bixuan:
                bi += [lst(jishu)]
            else:
                xuan += [lst(jishu)]
        else:
            L = lst(jishu)
            del L[0]
            del L[0]
            if val in bixuan:
                bi[len(bi) - 1] += L
            else:
                xuan[len(xuan) - 1] += L
        jishu += 1

# print(bi)
# print(xuan)

L_New = []
for lst in bi:
    L_New += [MakeWeek(lst)]
# 打开（或创建）一个文件用于写入
with open('./data/bi.json', 'w') as f:
    # 使用json.dump()方法将列表写入文件
    json.dump(L_New, f, indent=4)  # indent=4用于美化输出，使JSON文件更易读

L_New = []
for lst in xuan:
    L_New += [MakeWeek(lst)]
# 打开（或创建）一个文件用于写入
with open('./data/xuan.json', 'w') as f:
    # 使用json.dump()方法将列表写入文件
    json.dump(L_New, f, indent=4)  # indent=4用于美化输出，使JSON文件更易读
