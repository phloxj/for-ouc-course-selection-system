# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konxian.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"D:/BlueStacks/ico/\u9010\u706b\u5341\u4e09\u82f1\u6840/Aponia.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 90, 215, 116))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_yuan = QPushButton(self.layoutWidget)
        self.pushButton_yuan.setObjectName(u"pushButton_yuan")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pushButton_yuan)

        self.lineEdit_yuan = QLineEdit(self.layoutWidget)
        self.lineEdit_yuan.setObjectName(u"lineEdit_yuan")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_yuan)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.pushButton_openpy = QPushButton(self.layoutWidget)
        self.pushButton_openpy.setObjectName(u"pushButton_openpy")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_openpy)

        self.pushButton_output = QPushButton(self.layoutWidget)
        self.pushButton_output.setObjectName(u"pushButton_output")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.pushButton_output)

        self.pushButton_open = QPushButton(self.layoutWidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pushButton_open)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9009\u8bfe", None))
#if QT_CONFIG(tooltip)
        self.pushButton_yuan.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9'xuanke'\u7cfb\u5217", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_yuan.setText(QCoreApplication.translate("Form", u"\u6e90\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u65f6\u95f4\u6570\u636e", None))
        self.pushButton_openpy.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u65f6\u95f4\u6570\u636e", None))
        self.pushButton_output.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.pushButton_open.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u8f93\u51fa\u6587\u4ef6\u5939", None))
    # retranslateUi

