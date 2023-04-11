# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowsRNNtZ.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QStatusBar, QTextBrowser, QWidget)
import resource_file_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 832)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1171, 811))
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
        self.display_videos = QWidget()
        self.display_videos.setObjectName(u"display_videos")
        self.label_28 = QLabel(self.display_videos)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(330, 81, 441, 91))
        self.label_28.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.scrollArea_3 = QScrollArea(self.display_videos)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(329, 200, 441, 451))
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 439, 449))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.title_11 = QLabel(self.scrollAreaWidgetContents_4)
        self.title_11.setObjectName(u"title_11")
        self.title_11.setFont(font)
        self.title_11.setStyleSheet(u"color: gray")
        self.title_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.title_11, 0, 0, 1, 1)

        self.video_frame_0 = QFrame(self.scrollAreaWidgetContents_4)
        self.video_frame_0.setObjectName(u"video_frame_0")
        self.video_frame_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_frame_0.setStyleSheet(u"QPushButton{\n"
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
        self.video_frame_0.setFrameShape(QFrame.NoFrame)
        self.video_frame_0.setFrameShadow(QFrame.Raised)
        self.video_frame_0.setLineWidth(0)
        self.video_layout_0 = QHBoxLayout(self.video_frame_0)
        self.video_layout_0.setSpacing(0)
        self.video_layout_0.setObjectName(u"video_layout_0")
        self.video_layout_0.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.video_frame_0, 1, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.next_page_videos = QFrame(self.display_videos)
        self.next_page_videos.setObjectName(u"next_page_videos")
        self.next_page_videos.setGeometry(QRect(680, 681, 91, 51))
        self.next_page_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_videos.setStyleSheet(u"QPushButton{\n"
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
        self.next_page_videos.setFrameShape(QFrame.NoFrame)
        self.next_page_videos.setFrameShadow(QFrame.Raised)
        self.next_page_videos.setLineWidth(0)
        self.next_page_videos_layout = QHBoxLayout(self.next_page_videos)
        self.next_page_videos_layout.setSpacing(0)
        self.next_page_videos_layout.setObjectName(u"next_page_videos_layout")
        self.next_page_videos_layout.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.display_videos)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(290, 40, 521, 721))
        self.label_29.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_8 = QLabel(self.display_videos)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setGeometry(QRect(330, 80, 441, 91))
        self.title_8.setFont(font)
        self.title_8.setStyleSheet(u"color: gray")
        self.title_8.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.display_videos)
        self.label_29.raise_()
        self.label_28.raise_()
        self.scrollArea_3.raise_()
        self.next_page_videos.raise_()
        self.title_8.raise_()
        self.na9 = QWidget()
        self.na9.setObjectName(u"na9")
        self.stackedWidget.addWidget(self.na9)
        self.display_text = QWidget()
        self.display_text.setObjectName(u"display_text")
        self.label_26 = QLabel(self.display_text)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(290, 40, 521, 721))
        self.label_26.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_7 = QLabel(self.display_text)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setGeometry(QRect(330, 60, 441, 91))
        self.title_7.setFont(font)
        self.title_7.setStyleSheet(u"color: gray")
        self.title_7.setAlignment(Qt.AlignCenter)
        self.scrollArea_2 = QScrollArea(self.display_text)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(329, 179, 441, 451))
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 439, 449))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 2, 0, 1, 1)

        self.title_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setFont(font)
        self.title_9.setStyleSheet(u"color: gray")
        self.title_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.title_9, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(421, 300))
        self.textBrowser.setStyleSheet(u"QTextBrowser { background-color: rgb(70, 74, 95); }\n"
"")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scroll_layout_frame_2 = QFrame(self.display_text)
        self.scroll_layout_frame_2.setObjectName(u"scroll_layout_frame_2")
        self.scroll_layout_frame_2.setGeometry(QRect(329, 179, 441, 51))
        self.scroll_layout_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.scroll_layout_frame_2.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.scroll_layout_frame_2.setFrameShape(QFrame.NoFrame)
        self.scroll_layout_frame_2.setFrameShadow(QFrame.Raised)
        self.scroll_layout_frame_2.setLineWidth(0)
        self.scroll_widget_layout_2 = QHBoxLayout(self.scroll_layout_frame_2)
        self.scroll_widget_layout_2.setSpacing(0)
        self.scroll_widget_layout_2.setObjectName(u"scroll_widget_layout_2")
        self.scroll_widget_layout_2.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.display_text)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(330, 60, 441, 91))
        self.label_27.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.next_page_text = QFrame(self.display_text)
        self.next_page_text.setObjectName(u"next_page_text")
        self.next_page_text.setGeometry(QRect(680, 660, 91, 51))
        self.next_page_text.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_text.setStyleSheet(u"QPushButton{\n"
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
        self.next_page_text.setFrameShape(QFrame.NoFrame)
        self.next_page_text.setFrameShadow(QFrame.Raised)
        self.next_page_text.setLineWidth(0)
        self.next_page_text_layout = QHBoxLayout(self.next_page_text)
        self.next_page_text_layout.setSpacing(0)
        self.next_page_text_layout.setObjectName(u"next_page_text_layout")
        self.next_page_text_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.display_text)
        self.label_26.raise_()
        self.label_27.raise_()
        self.title_7.raise_()
        self.scrollArea_2.raise_()
        self.scroll_layout_frame_2.raise_()
        self.next_page_text.raise_()
        self.display_image = QWidget()
        self.display_image.setObjectName(u"display_image")
        self.label_22 = QLabel(self.display_image)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(330, 60, 441, 91))
        self.label_22.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #21252d;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_25 = QLabel(self.display_image)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(290, 40, 521, 721))
        self.label_25.setStyleSheet(u"QLabel {\n"
"\n"
"\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_4 = QLabel(self.display_image)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(330, 60, 441, 91))
        self.title_4.setFont(font)
        self.title_4.setStyleSheet(u"color: gray")
        self.title_4.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.display_image)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(329, 179, 441, 451))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 1546))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image_41 = QPushButton(self.scrollAreaWidgetContents)
        self.image_41.setObjectName(u"image_41")
        self.image_41.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_41, 33, 0, 1, 1)

        self.image_2 = QPushButton(self.scrollAreaWidgetContents)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_2, 3, 0, 1, 1)

        self.image_31 = QPushButton(self.scrollAreaWidgetContents)
        self.image_31.setObjectName(u"image_31")
        self.image_31.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_31, 32, 0, 1, 1)

        self.image_11 = QPushButton(self.scrollAreaWidgetContents)
        self.image_11.setObjectName(u"image_11")
        self.image_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_11, 12, 0, 1, 1)

        self.image_40 = QPushButton(self.scrollAreaWidgetContents)
        self.image_40.setObjectName(u"image_40")
        self.image_40.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_40, 47, 0, 1, 1)

        self.title_6 = QLabel(self.scrollAreaWidgetContents)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setFont(font)
        self.title_6.setStyleSheet(u"color: gray")
        self.title_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_6, 0, 0, 1, 1)

        self.image_26 = QPushButton(self.scrollAreaWidgetContents)
        self.image_26.setObjectName(u"image_26")
        self.image_26.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_26, 29, 0, 1, 1)

        self.image_36 = QPushButton(self.scrollAreaWidgetContents)
        self.image_36.setObjectName(u"image_36")
        self.image_36.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_36, 31, 0, 1, 1)

        self.image_21 = QPushButton(self.scrollAreaWidgetContents)
        self.image_21.setObjectName(u"image_21")
        self.image_21.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_21, 22, 0, 1, 1)

        self.image_8 = QPushButton(self.scrollAreaWidgetContents)
        self.image_8.setObjectName(u"image_8")
        self.image_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_8, 9, 0, 1, 1)

        self.image_0 = QPushButton(self.scrollAreaWidgetContents)
        self.image_0.setObjectName(u"image_0")
        self.image_0.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_0, 1, 0, 1, 1)

        self.image_13 = QPushButton(self.scrollAreaWidgetContents)
        self.image_13.setObjectName(u"image_13")
        self.image_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_13, 14, 0, 1, 1)

        self.image_10 = QPushButton(self.scrollAreaWidgetContents)
        self.image_10.setObjectName(u"image_10")
        self.image_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_10, 11, 0, 1, 1)

        self.image_15 = QPushButton(self.scrollAreaWidgetContents)
        self.image_15.setObjectName(u"image_15")
        self.image_15.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_15, 16, 0, 1, 1)

        self.image_38 = QPushButton(self.scrollAreaWidgetContents)
        self.image_38.setObjectName(u"image_38")
        self.image_38.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_38, 48, 0, 1, 1)

        self.image_3 = QPushButton(self.scrollAreaWidgetContents)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_3, 4, 0, 1, 1)

        self.image_47 = QPushButton(self.scrollAreaWidgetContents)
        self.image_47.setObjectName(u"image_47")
        self.image_47.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_47, 46, 0, 1, 1)

        self.image_9 = QPushButton(self.scrollAreaWidgetContents)
        self.image_9.setObjectName(u"image_9")
        self.image_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_9, 10, 0, 1, 1)

        self.image_18 = QPushButton(self.scrollAreaWidgetContents)
        self.image_18.setObjectName(u"image_18")
        self.image_18.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_18, 19, 0, 1, 1)

        self.image_12 = QPushButton(self.scrollAreaWidgetContents)
        self.image_12.setObjectName(u"image_12")
        self.image_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_12, 13, 0, 1, 1)

        self.image_6 = QPushButton(self.scrollAreaWidgetContents)
        self.image_6.setObjectName(u"image_6")
        self.image_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_6, 7, 0, 1, 1)

        self.image_5 = QPushButton(self.scrollAreaWidgetContents)
        self.image_5.setObjectName(u"image_5")
        self.image_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_5, 6, 0, 1, 1)

        self.image_19 = QPushButton(self.scrollAreaWidgetContents)
        self.image_19.setObjectName(u"image_19")
        self.image_19.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_19, 20, 0, 1, 1)

        self.image_37 = QPushButton(self.scrollAreaWidgetContents)
        self.image_37.setObjectName(u"image_37")
        self.image_37.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_37, 49, 0, 1, 1)

        self.image_1 = QPushButton(self.scrollAreaWidgetContents)
        self.image_1.setObjectName(u"image_1")
        self.image_1.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_1, 2, 0, 1, 1)

        self.image_49 = QPushButton(self.scrollAreaWidgetContents)
        self.image_49.setObjectName(u"image_49")
        self.image_49.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_49, 50, 0, 1, 1)

        self.image_28 = QPushButton(self.scrollAreaWidgetContents)
        self.image_28.setObjectName(u"image_28")
        self.image_28.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_28, 41, 0, 1, 1)

        self.image_35 = QPushButton(self.scrollAreaWidgetContents)
        self.image_35.setObjectName(u"image_35")
        self.image_35.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_35, 39, 0, 1, 1)

        self.image_39 = QPushButton(self.scrollAreaWidgetContents)
        self.image_39.setObjectName(u"image_39")
        self.image_39.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_39, 43, 0, 1, 1)

        self.image_4 = QPushButton(self.scrollAreaWidgetContents)
        self.image_4.setObjectName(u"image_4")
        self.image_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_4, 5, 0, 1, 1)

        self.image_45 = QPushButton(self.scrollAreaWidgetContents)
        self.image_45.setObjectName(u"image_45")
        self.image_45.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_45, 30, 0, 1, 1)

        self.image_48 = QPushButton(self.scrollAreaWidgetContents)
        self.image_48.setObjectName(u"image_48")
        self.image_48.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_48, 42, 0, 1, 1)

        self.image_20 = QPushButton(self.scrollAreaWidgetContents)
        self.image_20.setObjectName(u"image_20")
        self.image_20.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_20, 21, 0, 1, 1)

        self.image_27 = QPushButton(self.scrollAreaWidgetContents)
        self.image_27.setObjectName(u"image_27")
        self.image_27.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_27, 27, 0, 1, 1)

        self.image_14 = QPushButton(self.scrollAreaWidgetContents)
        self.image_14.setObjectName(u"image_14")
        self.image_14.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_14, 15, 0, 1, 1)

        self.image_33 = QPushButton(self.scrollAreaWidgetContents)
        self.image_33.setObjectName(u"image_33")
        self.image_33.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_33, 40, 0, 1, 1)

        self.image_29 = QPushButton(self.scrollAreaWidgetContents)
        self.image_29.setObjectName(u"image_29")
        self.image_29.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_29, 45, 0, 1, 1)

        self.image_16 = QPushButton(self.scrollAreaWidgetContents)
        self.image_16.setObjectName(u"image_16")
        self.image_16.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_16, 17, 0, 1, 1)

        self.image_43 = QPushButton(self.scrollAreaWidgetContents)
        self.image_43.setObjectName(u"image_43")
        self.image_43.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_43, 28, 0, 1, 1)

        self.image_23 = QPushButton(self.scrollAreaWidgetContents)
        self.image_23.setObjectName(u"image_23")
        self.image_23.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_23, 24, 0, 1, 1)

        self.image_22 = QPushButton(self.scrollAreaWidgetContents)
        self.image_22.setObjectName(u"image_22")
        self.image_22.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_22, 23, 0, 1, 1)

        self.image_46 = QPushButton(self.scrollAreaWidgetContents)
        self.image_46.setObjectName(u"image_46")
        self.image_46.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_46, 35, 0, 1, 1)

        self.image_34 = QPushButton(self.scrollAreaWidgetContents)
        self.image_34.setObjectName(u"image_34")
        self.image_34.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_34, 36, 0, 1, 1)

        self.image_7 = QPushButton(self.scrollAreaWidgetContents)
        self.image_7.setObjectName(u"image_7")
        self.image_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_7, 8, 0, 1, 1)

        self.image_17 = QPushButton(self.scrollAreaWidgetContents)
        self.image_17.setObjectName(u"image_17")
        self.image_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_17, 18, 0, 1, 1)

        self.image_30 = QPushButton(self.scrollAreaWidgetContents)
        self.image_30.setObjectName(u"image_30")
        self.image_30.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_30, 34, 0, 1, 1)

        self.image_44 = QPushButton(self.scrollAreaWidgetContents)
        self.image_44.setObjectName(u"image_44")
        self.image_44.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_44, 26, 0, 1, 1)

        self.image_25 = QPushButton(self.scrollAreaWidgetContents)
        self.image_25.setObjectName(u"image_25")
        self.image_25.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_25, 38, 0, 1, 1)

        self.image_24 = QPushButton(self.scrollAreaWidgetContents)
        self.image_24.setObjectName(u"image_24")
        self.image_24.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_24, 25, 0, 1, 1)

        self.image_32 = QPushButton(self.scrollAreaWidgetContents)
        self.image_32.setObjectName(u"image_32")
        self.image_32.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_32, 44, 0, 1, 1)

        self.image_42 = QPushButton(self.scrollAreaWidgetContents)
        self.image_42.setObjectName(u"image_42")
        self.image_42.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")

        self.gridLayout.addWidget(self.image_42, 37, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.next_page_image = QFrame(self.display_image)
        self.next_page_image.setObjectName(u"next_page_image")
        self.next_page_image.setGeometry(QRect(680, 660, 91, 51))
        self.next_page_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_page_image.setStyleSheet(u"QPushButton{\n"
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
        self.next_page_image.setFrameShape(QFrame.NoFrame)
        self.next_page_image.setFrameShadow(QFrame.Raised)
        self.next_page_image.setLineWidth(0)
        self.next_page_image_layout = QHBoxLayout(self.next_page_image)
        self.next_page_image_layout.setSpacing(0)
        self.next_page_image_layout.setObjectName(u"next_page_image_layout")
        self.next_page_image_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.display_image)
        self.label_25.raise_()
        self.label_22.raise_()
        self.title_4.raise_()
        self.scrollArea.raise_()
        self.next_page_image.raise_()
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
        self.label_28.setText("")
        self.title_11.setText(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.label_29.setText("")
        self.title_8.setText(QCoreApplication.translate("MainWindow", u"Fluorite Scrape", None))
        self.label_26.setText("")
        self.title_7.setText(QCoreApplication.translate("MainWindow", u"Fluorite Scrape", None))
        self.title_9.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_27.setText("")
        self.label_22.setText("")
        self.label_25.setText("")
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Fluorite Scrape", None))
        self.image_41.setText("")
        self.image_2.setText("")
        self.image_31.setText("")
        self.image_11.setText("")
        self.image_40.setText("")
        self.title_6.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.image_26.setText("")
        self.image_36.setText("")
        self.image_21.setText("")
        self.image_8.setText("")
        self.image_0.setText("")
        self.image_13.setText("")
        self.image_10.setText("")
        self.image_15.setText("")
        self.image_38.setText("")
        self.image_3.setText("")
        self.image_47.setText("")
        self.image_9.setText("")
        self.image_18.setText("")
        self.image_12.setText("")
        self.image_6.setText("")
        self.image_5.setText("")
        self.image_19.setText("")
        self.image_37.setText("")
        self.image_1.setText("")
        self.image_49.setText("")
        self.image_28.setText("")
        self.image_35.setText("")
        self.image_39.setText("")
        self.image_4.setText("")
        self.image_45.setText("")
        self.image_48.setText("")
        self.image_20.setText("")
        self.image_27.setText("")
        self.image_14.setText("")
        self.image_33.setText("")
        self.image_29.setText("")
        self.image_16.setText("")
        self.image_43.setText("")
        self.image_23.setText("")
        self.image_22.setText("")
        self.image_46.setText("")
        self.image_34.setText("")
        self.image_7.setText("")
        self.image_17.setText("")
        self.image_30.setText("")
        self.image_44.setText("")
        self.image_25.setText("")
        self.image_24.setText("")
        self.image_32.setText("")
        self.image_42.setText("")
    # retranslateUi

