import os
import subprocess

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from konxian import Ui_Form
from get_pre_json import get_json
from contrast_json import get_clash_json
from write_not_clash import write_clash


def openpy():
    subprocess.run(['python', "xuanke_main.py"], capture_output=True, text=True)


def start_file():
    folder_path = '.\\output'
    os.startfile(folder_path)


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        self.file_path = ''

    def bind(self):
        self.pushButton_yuan.clicked.connect(self.open_file_dialog)
        self.pushButton_openpy.clicked.connect(openpy)
        self.pushButton_output.clicked.connect(self.output)
        self.pushButton_open.clicked.connect(start_file)

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "C:/Users/qwe_r/Documents/选课",  # 默认目录
                                                        "Excel Files (*.xlsx)")
        print(self.file_path)
        folder_path, file_name = os.path.split(self.file_path)
        self.lineEdit_yuan.setText(file_name)

    def output(self):
        # xuanke_xlsx = self.lineEdit_yuan.text()
        get_json(self.file_path)
        get_clash_json()
        write_clash(self.file_path)
        QMessageBox.information(self, '提示', '操作成功', QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
