import os

import openpyxl
import json
from datetime import datetime

from openpyxl.workbook import Workbook


# read_path_xlsx = 'C:/Users/qwe_r/Documents/选课/xuanke20232.xlsx'
def write_clash(read_path_xlsx):
    read_path_json = './data/not_clash.json'

    _, file_name = os.path.split(read_path_xlsx)
    now = datetime.now()  # 获取当前时间
    formatted_now = now.strftime('%Y%m%d_%H%M%S_')
    write_path = './output/' + formatted_now + file_name

    with open(read_path_json, 'r') as f:
        # 使用json.load()读取文件内容并解码成Python对象
        not_clash = json.load(f)

    def lst(ji):
        return [cell.value for cell in sheet[ji]]

    def write_to_excel(file_path0, data):
        # 创建一个新的工作簿
        wb = Workbook()
        # 激活默认的工作表
        ws = wb.active
        # 遍历二维列表，将数据写入工作表
        for row in data:
            ws.append(row)
            # 保存工作簿到文件
        wb.save(file_path0)

    output = []
    # 打开工作表
    file_path = read_path_xlsx  # 打开路径
    workbook = openpyxl.load_workbook(file_path)
    kcfw = ['Specialty', 'Common', 'PublicBasic']  # 课程范围
    for kc in kcfw:
        sheet_name = kc
        sheet = workbook[sheet_name]
        column_values = [cell.value for cell in sheet['A']]
        jishu = 1
        is_before = False
        for value in column_values:
            if value is not None:
                if value in not_clash:
                    is_before = True
                    output += [lst(jishu)]
                else:
                    is_before = False
            else:
                if is_before:
                    output += [lst(jishu)]

            jishu += 1
    write_to_excel(write_path, output)
