# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowYntfAV.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTextBrowser, QWidget)
import resource_file_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 833)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -1, 1171, 811))
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.label_19 = QLabel(self.Main)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(330, 90, 441, 91))
        self.label_19.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_3 = QLabel(self.Main)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(370, 120, 351, 41))
        font = QFont()
        font.setPointSize(16)
        self.title_3.setFont(font)
        self.title_3.setStyleSheet(u"color: gray")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.label_24 = QLabel(self.Main)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(290, 70, 521, 721))
        self.label_24.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.url_input = QLineEdit(self.Main)
        self.url_input.setObjectName(u"url_input")
        self.url_input.setGeometry(QRect(330, 230, 441, 51))
        self.url_input.setStyleSheet(u"color: gray;\n"
"background-color: rgb(63, 67, 86);\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(73, 88, 97);")
        self.text_frame = QFrame(self.Main)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setGeometry(QRect(520, 360, 241, 91))
        self.text_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.text_frame.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.text_frame.setFrameShape(QFrame.NoFrame)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.text_frame.setLineWidth(0)
        self.text_layout = QHBoxLayout(self.text_frame)
        self.text_layout.setSpacing(0)
        self.text_layout.setObjectName(u"text_layout")
        self.text_layout.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.Main)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(331, 360, 171, 91))
        self.label_23.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: rgba(33,37,45,140);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_4 = QLabel(self.Main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 390, 141, 31))
        self.label_4.setStyleSheet(u"color: gray")
        self.label_4.setWordWrap(True)
        self.images_frame = QFrame(self.Main)
        self.images_frame.setObjectName(u"images_frame")
        self.images_frame.setGeometry(QRect(520, 470, 241, 91))
        self.images_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.images_frame.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.images_frame.setFrameShape(QFrame.NoFrame)
        self.images_frame.setFrameShadow(QFrame.Raised)
        self.images_frame.setLineWidth(0)
        self.images_layout = QHBoxLayout(self.images_frame)
        self.images_layout.setSpacing(0)
        self.images_layout.setObjectName(u"images_layout")
        self.images_layout.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.Main)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 470, 171, 91))
        self.label_20.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: rgba(33,37,45,140);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_6 = QLabel(self.Main)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 500, 141, 31))
        self.label_6.setStyleSheet(u"color: gray")
        self.label_6.setWordWrap(True)
        self.videos_frame = QFrame(self.Main)
        self.videos_frame.setObjectName(u"videos_frame")
        self.videos_frame.setGeometry(QRect(520, 580, 241, 91))
        self.videos_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.videos_frame.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.videos_frame.setFrameShape(QFrame.NoFrame)
        self.videos_frame.setFrameShadow(QFrame.Raised)
        self.videos_frame.setLineWidth(0)
        self.videos_layout = QHBoxLayout(self.videos_frame)
        self.videos_layout.setSpacing(0)
        self.videos_layout.setObjectName(u"videos_layout")
        self.videos_layout.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.Main)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(331, 580, 171, 91))
        self.label_21.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: rgba(33,37,45,140);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_5 = QLabel(self.Main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 610, 131, 31))
        self.label_5.setStyleSheet(u"color: gray")
        self.label_98 = QLabel(self.Main)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(320, 330, 461, 431))
        self.label_98.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(70, 74, 95);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_99 = QLabel(self.Main)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(320, 200, 461, 111))
        self.label_99.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(70, 74, 95);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_115 = QLabel(self.Main)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(520, 360, 241, 91))
        self.label_115.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_116 = QLabel(self.Main)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(520, 470, 241, 91))
        self.label_116.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_117 = QLabel(self.Main)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(520, 580, 241, 91))
        self.label_117.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.status_bar = QFrame(self.Main)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setGeometry(QRect(330, 690, 431, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.status_bar.setFont(font1)
        self.status_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_bar.setStyleSheet(u"color: gray;\n"
"font: 12pt \"Segoe UI\";")
        self.status_bar.setFrameShape(QFrame.NoFrame)
        self.status_bar.setFrameShadow(QFrame.Raised)
        self.status_bar.setLineWidth(0)
        self.status_bar_layout = QHBoxLayout(self.status_bar)
        self.status_bar_layout.setSpacing(0)
        self.status_bar_layout.setObjectName(u"status_bar_layout")
        self.status_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.Main)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(330, 690, 431, 51))
        self.label_118.setStyleSheet(u"color: gray;\n"
"background-color: rgb(63, 67, 86);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 237, 194, 40);")
        self.stackedWidget.addWidget(self.Main)
        self.label_24.raise_()
        self.label_98.raise_()
        self.label_118.raise_()
        self.label_117.raise_()
        self.label_116.raise_()
        self.label_115.raise_()
        self.label_99.raise_()
        self.label_19.raise_()
        self.title_3.raise_()
        self.url_input.raise_()
        self.text_frame.raise_()
        self.label_23.raise_()
        self.label_4.raise_()
        self.images_frame.raise_()
        self.label_20.raise_()
        self.label_6.raise_()
        self.videos_frame.raise_()
        self.label_21.raise_()
        self.label_5.raise_()
        self.status_bar.raise_()
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.misc_keep = QWidget()
        self.misc_keep.setObjectName(u"misc_keep")
        self.manage_buckets_frame_2 = QFrame(self.misc_keep)
        self.manage_buckets_frame_2.setObjectName(u"manage_buckets_frame_2")
        self.manage_buckets_frame_2.setGeometry(QRect(570, 240, 131, 71))
        self.manage_buckets_frame_2.setStyleSheet(u"")
        self.manage_buckets_frame_2.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_2.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_2.setLineWidth(0)
        self.settings_toggle_1_layout = QHBoxLayout(self.manage_buckets_frame_2)
        self.settings_toggle_1_layout.setSpacing(0)
        self.settings_toggle_1_layout.setObjectName(u"settings_toggle_1_layout")
        self.settings_toggle_1_layout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.misc_keep)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 230, 171, 91))
        self.label_11.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #272c36;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_12 = QLabel(self.misc_keep)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(330, 330, 171, 91))
        self.label_12.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #272c36;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_13 = QLabel(self.misc_keep)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(330, 430, 171, 91))
        self.label_13.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #272c36;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.manage_buckets_frame_3 = QFrame(self.misc_keep)
        self.manage_buckets_frame_3.setObjectName(u"manage_buckets_frame_3")
        self.manage_buckets_frame_3.setGeometry(QRect(570, 340, 131, 71))
        self.manage_buckets_frame_3.setStyleSheet(u"")
        self.manage_buckets_frame_3.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_3.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_3.setLineWidth(0)
        self.settings_toggle_2_layout = QHBoxLayout(self.manage_buckets_frame_3)
        self.settings_toggle_2_layout.setSpacing(0)
        self.settings_toggle_2_layout.setObjectName(u"settings_toggle_2_layout")
        self.settings_toggle_2_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_buckets_frame_4 = QFrame(self.misc_keep)
        self.manage_buckets_frame_4.setObjectName(u"manage_buckets_frame_4")
        self.manage_buckets_frame_4.setGeometry(QRect(570, 440, 131, 71))
        self.manage_buckets_frame_4.setStyleSheet(u"")
        self.manage_buckets_frame_4.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_4.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_4.setLineWidth(0)
        self.settings_toggle_3_layout = QHBoxLayout(self.manage_buckets_frame_4)
        self.settings_toggle_3_layout.setSpacing(0)
        self.settings_toggle_3_layout.setObjectName(u"settings_toggle_3_layout")
        self.settings_toggle_3_layout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.misc_keep)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 120, 441, 91))
        self.label_14.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_2 = QLabel(self.misc_keep)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(370, 150, 351, 41))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"color: gray")
        self.title_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.misc_keep)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 260, 81, 31))
        self.label.setStyleSheet(u"color: gray")
        self.label_2 = QLabel(self.misc_keep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 360, 141, 31))
        self.label_2.setStyleSheet(u"color: gray")
        self.label_3 = QLabel(self.misc_keep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 460, 131, 31))
        self.label_3.setStyleSheet(u"color: gray")
        self.label_15 = QLabel(self.misc_keep)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(510, 230, 251, 91))
        self.label_15.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_16 = QLabel(self.misc_keep)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(510, 330, 251, 91))
        self.label_16.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_17 = QLabel(self.misc_keep)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(510, 430, 251, 91))
        self.label_17.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_18 = QLabel(self.misc_keep)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(290, 100, 521, 471))
        self.label_18.setStyleSheet(u"QLabel {\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_8 = QFrame(self.misc_keep)
        self.back_button_frame_8.setObjectName(u"back_button_frame_8")
        self.back_button_frame_8.setGeometry(QRect(860, 580, 261, 61))
        self.back_button_frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_8.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(60, 64, 82);\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: 462e2e;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(134, 88, 88);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(66, 134, 132);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_8.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_8.setFrameShadow(QFrame.Raised)
        self.back_button_frame_8.setLineWidth(0)
        self.return_home_layout_settings = QHBoxLayout(self.back_button_frame_8)
        self.return_home_layout_settings.setSpacing(0)
        self.return_home_layout_settings.setObjectName(u"return_home_layout_settings")
        self.return_home_layout_settings.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.misc_keep)
        self.label_18.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.manage_buckets_frame_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.manage_buckets_frame_3.raise_()
        self.manage_buckets_frame_4.raise_()
        self.label_14.raise_()
        self.title_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.back_button_frame_8.raise_()
        self.na10 = QWidget()
        self.na10.setObjectName(u"na10")
        self.stackedWidget.addWidget(self.na10)
        self.na9 = QWidget()
        self.na9.setObjectName(u"na9")
        self.stackedWidget.addWidget(self.na9)
        self.na1 = QWidget()
        self.na1.setObjectName(u"na1")
        self.stackedWidget.addWidget(self.na1)
        self.Display = QWidget()
        self.Display.setObjectName(u"Display")
        self.label_22 = QLabel(self.Display)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(330, 90, 441, 91))
        self.label_22.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_25 = QLabel(self.Display)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(290, 70, 521, 721))
        self.label_25.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_4 = QLabel(self.Display)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(330, 90, 441, 91))
        self.title_4.setFont(font)
        self.title_4.setStyleSheet(u"color: gray")
        self.title_4.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.Display)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(329, 209, 441, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 439, 539))
        self.title_5 = QLabel(self.scrollAreaWidgetContents)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setGeometry(QRect(0, 10, 451, 41))
        self.title_5.setFont(font)
        self.title_5.setStyleSheet(u"color: gray")
        self.title_5.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 50, 421, 192))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.Display)
        self.label_25.raise_()
        self.label_22.raise_()
        self.title_4.raise_()
        self.scrollArea.raise_()
        self.na8 = QWidget()
        self.na8.setObjectName(u"na8")
        self.stackedWidget.addWidget(self.na8)
        self.na3 = QWidget()
        self.na3.setObjectName(u"na3")
        self.stackedWidget.addWidget(self.na3)
        self.na4 = QWidget()
        self.na4.setObjectName(u"na4")
        self.stackedWidget.addWidget(self.na4)
        self.na5 = QWidget()
        self.na5.setObjectName(u"na5")
        self.stackedWidget.addWidget(self.na5)
        self.na6 = QWidget()
        self.na6.setObjectName(u"na6")
        self.stackedWidget.addWidget(self.na6)
        self.na7 = QWidget()
        self.na7.setObjectName(u"na7")
        self.stackedWidget.addWidget(self.na7)
        self.na2 = QWidget()
        self.na2.setObjectName(u"na2")
        self.stackedWidget.addWidget(self.na2)
        self.app_install_frame_6 = QFrame(self.centralwidget)
        self.app_install_frame_6.setObjectName(u"app_install_frame_6")
        self.app_install_frame_6.setGeometry(QRect(690, 230, 91, 51))
        self.app_install_frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 9pt \"Segoe UI\";\n"
"	background-color: rgb(89, 93, 117);\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"	border: 2px solid rgb(73, 88, 97);\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(66, 134, 132);\n"
"	border-bottom-right-radius: 25px;\n"
"	border-top-right-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.app_install_frame_6.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_6.setFrameShadow(QFrame.Raised)
        self.app_install_frame_6.setLineWidth(0)
        self.scrape_layout = QHBoxLayout(self.app_install_frame_6)
        self.scrape_layout.setSpacing(0)
        self.scrape_layout.setObjectName(u"scrape_layout")
        self.scrape_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_19.setText("")
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Fluorite Scrape", None))
        self.label_24.setText("")
        self.url_input.setText(QCoreApplication.translate("MainWindow", u"Enter Url for website to scrape", None))
        self.label_23.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_20.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.label_21.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.label_98.setText("")
        self.label_99.setText("")
        self.label_115.setText("")
        self.label_116.setText("")
        self.label_117.setText("")
        self.label_118.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Faster Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Use Download Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Some other setting", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_22.setText("")
        self.label_25.setText("")
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Fluorite Scrape", None))
        self.title_5.setText(QCoreApplication.translate("MainWindow", u"Text", None))
    # retranslateUi

