import json

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from xuanke import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        self.output = [
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False]
        ]

    def bind(self):
        self.pushButton_1_1.clicked.connect(lambda: self.change(1, 1, self.pushButton_1_1))
        self.pushButton_1_2.clicked.connect(lambda: self.change(1, 2, self.pushButton_1_2))
        self.pushButton_1_3.clicked.connect(lambda: self.change(1, 3, self.pushButton_1_3))
        self.pushButton_1_4.clicked.connect(lambda: self.change(1, 4, self.pushButton_1_4))
        self.pushButton_1_5.clicked.connect(lambda: self.change(1, 5, self.pushButton_1_5))
        self.pushButton_1_6.clicked.connect(lambda: self.change(1, 6, self.pushButton_1_6))
        self.pushButton_1_7.clicked.connect(lambda: self.change(1, 7, self.pushButton_1_7))
        self.pushButton_1_8.clicked.connect(lambda: self.change(1, 8, self.pushButton_1_8))
        self.pushButton_1_9.clicked.connect(lambda: self.change(1, 9, self.pushButton_1_9))
        self.pushButton_1_10.clicked.connect(lambda: self.change(1, 10, self.pushButton_1_10))
        self.pushButton_1_11.clicked.connect(lambda: self.change(1, 11, self.pushButton_1_11))
        self.pushButton_1_12.clicked.connect(lambda: self.change(1, 12, self.pushButton_1_12))
        self.pushButton_2_1.clicked.connect(lambda: self.change(2, 1, self.pushButton_2_1))
        self.pushButton_2_2.clicked.connect(lambda: self.change(2, 2, self.pushButton_2_2))
        self.pushButton_2_3.clicked.connect(lambda: self.change(2, 3, self.pushButton_2_3))
        self.pushButton_2_4.clicked.connect(lambda: self.change(2, 4, self.pushButton_2_4))
        self.pushButton_2_5.clicked.connect(lambda: self.change(2, 5, self.pushButton_2_5))
        self.pushButton_2_6.clicked.connect(lambda: self.change(2, 6, self.pushButton_2_6))
        self.pushButton_2_7.clicked.connect(lambda: self.change(2, 7, self.pushButton_2_7))
        self.pushButton_2_8.clicked.connect(lambda: self.change(2, 8, self.pushButton_2_8))
        self.pushButton_2_9.clicked.connect(lambda: self.change(2, 9, self.pushButton_2_9))
        self.pushButton_2_10.clicked.connect(lambda: self.change(2, 10, self.pushButton_2_10))
        self.pushButton_2_11.clicked.connect(lambda: self.change(2, 11, self.pushButton_2_11))
        self.pushButton_2_12.clicked.connect(lambda: self.change(2, 12, self.pushButton_2_12))
        self.pushButton_3_1.clicked.connect(lambda: self.change(3, 1, self.pushButton_3_1))
        self.pushButton_3_2.clicked.connect(lambda: self.change(3, 2, self.pushButton_3_2))
        self.pushButton_3_3.clicked.connect(lambda: self.change(3, 3, self.pushButton_3_3))
        self.pushButton_3_4.clicked.connect(lambda: self.change(3, 4, self.pushButton_3_4))
        self.pushButton_3_5.clicked.connect(lambda: self.change(3, 5, self.pushButton_3_5))
        self.pushButton_3_6.clicked.connect(lambda: self.change(3, 6, self.pushButton_3_6))
        self.pushButton_3_7.clicked.connect(lambda: self.change(3, 7, self.pushButton_3_7))
        self.pushButton_3_8.clicked.connect(lambda: self.change(3, 8, self.pushButton_3_8))
        self.pushButton_3_9.clicked.connect(lambda: self.change(3, 9, self.pushButton_3_9))
        self.pushButton_3_10.clicked.connect(lambda: self.change(3, 10, self.pushButton_3_10))
        self.pushButton_3_11.clicked.connect(lambda: self.change(3, 11, self.pushButton_3_11))
        self.pushButton_3_12.clicked.connect(lambda: self.change(3, 12, self.pushButton_3_12))
        self.pushButton_4_1.clicked.connect(lambda: self.change(4, 1, self.pushButton_4_1))
        self.pushButton_4_2.clicked.connect(lambda: self.change(4, 2, self.pushButton_4_2))
        self.pushButton_4_3.clicked.connect(lambda: self.change(4, 3, self.pushButton_4_3))
        self.pushButton_4_4.clicked.connect(lambda: self.change(4, 4, self.pushButton_4_4))
        self.pushButton_4_5.clicked.connect(lambda: self.change(4, 5, self.pushButton_4_5))
        self.pushButton_4_6.clicked.connect(lambda: self.change(4, 6, self.pushButton_4_6))
        self.pushButton_4_7.clicked.connect(lambda: self.change(4, 7, self.pushButton_4_7))
        self.pushButton_4_8.clicked.connect(lambda: self.change(4, 8, self.pushButton_4_8))
        self.pushButton_4_9.clicked.connect(lambda: self.change(4, 9, self.pushButton_4_9))
        self.pushButton_4_10.clicked.connect(lambda: self.change(4, 10, self.pushButton_4_10))
        self.pushButton_4_11.clicked.connect(lambda: self.change(4, 11, self.pushButton_4_11))
        self.pushButton_4_12.clicked.connect(lambda: self.change(4, 12, self.pushButton_4_12))
        self.pushButton_5_1.clicked.connect(lambda: self.change(5, 1, self.pushButton_5_1))
        self.pushButton_5_2.clicked.connect(lambda: self.change(5, 2, self.pushButton_5_2))
        self.pushButton_5_3.clicked.connect(lambda: self.change(5, 3, self.pushButton_5_3))
        self.pushButton_5_4.clicked.connect(lambda: self.change(5, 4, self.pushButton_5_4))
        self.pushButton_5_5.clicked.connect(lambda: self.change(5, 5, self.pushButton_5_5))
        self.pushButton_5_6.clicked.connect(lambda: self.change(5, 6, self.pushButton_5_6))
        self.pushButton_5_7.clicked.connect(lambda: self.change(5, 7, self.pushButton_5_7))
        self.pushButton_5_8.clicked.connect(lambda: self.change(5, 8, self.pushButton_5_8))
        self.pushButton_5_9.clicked.connect(lambda: self.change(5, 9, self.pushButton_5_9))
        self.pushButton_5_10.clicked.connect(lambda: self.change(5, 10, self.pushButton_5_10))
        self.pushButton_5_11.clicked.connect(lambda: self.change(5, 11, self.pushButton_5_11))
        self.pushButton_5_12.clicked.connect(lambda: self.change(5, 12, self.pushButton_5_12))
        self.pushButton_6_1.clicked.connect(lambda: self.change(6, 1, self.pushButton_6_1))
        self.pushButton_6_2.clicked.connect(lambda: self.change(6, 2, self.pushButton_6_2))
        self.pushButton_6_3.clicked.connect(lambda: self.change(6, 3, self.pushButton_6_3))
        self.pushButton_6_4.clicked.connect(lambda: self.change(6, 4, self.pushButton_6_4))
        self.pushButton_6_5.clicked.connect(lambda: self.change(6, 5, self.pushButton_6_5))
        self.pushButton_6_6.clicked.connect(lambda: self.change(6, 6, self.pushButton_6_6))
        self.pushButton_6_7.clicked.connect(lambda: self.change(6, 7, self.pushButton_6_7))
        self.pushButton_6_8.clicked.connect(lambda: self.change(6, 8, self.pushButton_6_8))
        self.pushButton_6_9.clicked.connect(lambda: self.change(6, 9, self.pushButton_6_9))
        self.pushButton_6_10.clicked.connect(lambda: self.change(6, 10, self.pushButton_6_10))
        self.pushButton_6_11.clicked.connect(lambda: self.change(6, 11, self.pushButton_6_11))
        self.pushButton_6_12.clicked.connect(lambda: self.change(6, 12, self.pushButton_6_12))
        self.pushButton_7_1.clicked.connect(lambda: self.change(7, 1, self.pushButton_7_1))
        self.pushButton_7_2.clicked.connect(lambda: self.change(7, 2, self.pushButton_7_2))
        self.pushButton_7_3.clicked.connect(lambda: self.change(7, 3, self.pushButton_7_3))
        self.pushButton_7_4.clicked.connect(lambda: self.change(7, 4, self.pushButton_7_4))
        self.pushButton_7_5.clicked.connect(lambda: self.change(7, 5, self.pushButton_7_5))
        self.pushButton_7_6.clicked.connect(lambda: self.change(7, 6, self.pushButton_7_6))
        self.pushButton_7_7.clicked.connect(lambda: self.change(7, 7, self.pushButton_7_7))
        self.pushButton_7_8.clicked.connect(lambda: self.change(7, 8, self.pushButton_7_8))
        self.pushButton_7_9.clicked.connect(lambda: self.change(7, 9, self.pushButton_7_9))
        self.pushButton_7_10.clicked.connect(lambda: self.change(7, 10, self.pushButton_7_10))
        self.pushButton_7_11.clicked.connect(lambda: self.change(7, 11, self.pushButton_7_11))
        self.pushButton_7_12.clicked.connect(lambda: self.change(7, 12, self.pushButton_7_12))

        self.pushButton_save.clicked.connect(self.save_data)

    def change(self, zou, jie, button):
        # lambda中无法使用self.sender()
        # button = self.sender()
        # 检查按钮的当前样式表，如果它是默认的（或白色），则改为红色
        if not self.output[zou - 1][jie - 1]:  # 或者使用更复杂的逻辑来检查背景色
            button.setStyleSheet('background-color: #00ff00;')
            button.setText("选中")
            self.output[zou - 1][jie - 1] = True
        else:
            # 如果已经设置了样式表（即已经是红色或其他颜色），则可以选择恢复为白色
            button.setStyleSheet('')  # 恢复为默认样式表（可能是白色，也可能是Qt主题的其他颜色）
            button.setText("未选中")
            self.output[zou - 1][jie - 1] = False

    def save_data(self):
        with open('./data/output.json', 'w') as f:
            # 使用json.dump()方法将列表写入文件
            json.dump(self.output, f, indent=4)  # indent=4用于美化输出，使JSON文件更易读
        QMessageBox.information(self, '提示', '保存成功', QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
