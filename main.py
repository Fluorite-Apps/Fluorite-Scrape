# Imports
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from yt_dlp import *
import os.path
import sys
import os
from ui_window import *
from PySide6.QtGui import *
import subprocess
import re
from PySide6 import QtCore, QtWidgets, QtGui
import traceback
from PIL import Image

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QWidget, QMessageBox, QComboBox)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from state_tooltip import StateTooltip
from py_toggle import *
from Second_PushButton import *
from BlurWindow.blurWindow import blur
from BlurWindow.blurWindow import GlobalBlur
import resource_file_qt_rc
import subprocess
import plyer
from plyer import *
from plyer import notification
import shutil
from threading import Thread

from PySide6.QtCore import QUrl
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer

import cv2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# Global Variables
global url

# Create all files and folders if they don't exist
if not os.path.isdir('temp/'):
    os.mkdir('temp/')
if not os.path.isdir('temp/images/'):
    os.mkdir('temp/images/')
if not os.path.isdir('temp/videos/'):
    os.mkdir('temp/videos/')
if not os.path.isdir('temp/error/'):
    os.mkdir('temp/error/')


def notify_in_thread(title_prompt, message_prompt):
    notification.notify(
        title=(title_prompt),
        message=(message_prompt),
        app_icon="fluorite.ico",
        timeout=10,
    )


# def notify_in_thread(title_prompt, message_prompt):
#     thread_notify = Thread(target=notify_function)
#     thread_notify.daemon = True
#     thread_notify.start()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1150, 800)

        GlobalBlur(self.winId(), Dark=True, QWidget=self)

        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

        ################################################################################################################
        # MENU PAGE                                                                                                    #
        ################################################################################################################
        self.text_toggle = PyToggle(
            width=50
        )
        self.text_layout.addWidget(self.text_toggle, Qt.AlignCenter, Qt.AlignCenter)

        self.images_toggle = PyToggle(
            width=50
        )
        self.images_layout.addWidget(self.images_toggle, Qt.AlignCenter, Qt.AlignCenter)

        self.videos_toggle = PyToggle(
            width=50
        )
        self.videos_layout.addWidget(self.videos_toggle, Qt.AlignCenter, Qt.AlignCenter)

        self.scrape_button = custompushbutton('scrape', parent=self)
        self.scrape_button.setMinimumHeight(51)  # was 91
        self.scrape_button.setFixedWidth(91)  # was 251
        self.scrape_layout.addWidget(self.scrape_button, Qt.AlignCenter, Qt.AlignCenter)

        # status indicator
        self.status_bar_text = QLabel("", parent=self)
        self.status_bar_layout.addWidget(self.status_bar_text, Qt.AlignCenter, Qt.AlignCenter)

        self.text_next_button = custompushbutton('Next', parent=self)
        self.text_next_button.clicked.connect(lambda: go_to_next_page())
        self.next_page_text_layout.addWidget(self.text_next_button, Qt.AlignCenter, Qt.AlignCenter)
        self.image_next_button = custompushbutton('Next', parent=self)
        self.image_next_button.clicked.connect(lambda: go_to_next_page())
        self.next_page_image_layout.addWidget(self.image_next_button, Qt.AlignCenter, Qt.AlignCenter)
        self.videos_next_button = custompushbutton('Next', parent=self)
        self.videos_next_button.clicked.connect(lambda: go_to_next_page())
        self.next_page_videos_layout.addWidget(self.videos_next_button, Qt.AlignCenter, Qt.AlignCenter)

        def go_to_next_page():
            if str(self.stackedWidget.currentWidget().objectName()) == str("display_text"):
                self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, "display_image"))
            elif str(self.stackedWidget.currentWidget().objectName()) == str("display_image"):
                self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, "display_videos"))
            elif str(self.stackedWidget.currentWidget().objectName()) == str("display_videos"):
                self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, "display_text"))
            else:
                self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QtWidgets.QWidget, "display_text"))

        def scrape_in_thread():
            # Threads
            thread_scrape = Thread(target=scrape_gui)
            thread_scrape.daemon = True
            thread_scrape.start()

        self.scrape_button.clicked.connect(lambda: scrape_in_thread())

        def scrape_gui():

            # Deleting all temp files
            filelist = [f for f in os.listdir('temp/images/') if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join('temp/images/', f))
            for dirpath, dirnames, filenames in os.walk('temp/videos', topdown=False):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    os.remove(file_path)

                for dirname in dirnames:
                    dir_path = os.path.join(dirpath, dirname)
                    os.rmdir(dir_path)

            with open('temp/text.txt', 'w+') as f:
                f.truncate(0)
                f.seek(0)
            # Scraping
            global url
            url = self.url_input.text()
            notify_in_thread(title_prompt="Scraping", message_prompt=('Started to scrape website'))
            self.status_bar_text.setText("Started to scrape website")
            try:
                self.status_bar_text.setText("Initialising Webdriver")
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
            except Exception as e:
                notify_in_thread(title_prompt="Failed", message_prompt=('Invalid Url or Chrome driver'))
                self.status_bar_text.setText("Invalid Url or Chrome driver")
                with open('temp/error/error.txt', 'w+') as error:
                    error.truncate(0)
                    error.write(str(e))
                return
            time.sleep(5)

            if self.text_toggle.isChecked() == True:
                self.status_bar_text.setText("Scraping text")
                try:
                    with open('temp/text.txt', 'w+', encoding="utf-8") as web_text:
                        web_text.truncate(0)
                        web_text.seek(0)
                        self.status_bar_text.setText("Writing text to file temp/text.txt")
                        scraped_text = str(driver.find_element(By.XPATH, "/html/body").text)
                        web_text.write(scraped_text)
                        self.textBrowser.insertPlainText(scraped_text)
                except:
                    traceback.print_exc()
                    notify_in_thread(title_prompt="Failed", message_prompt=('Something went wrong'))
                    self.status_bar_text.setText("Something went wrong")

            if self.images_toggle.isChecked() == True:
                self.status_bar_text.setText("Scraping images")
                try:
                    self.status_bar_text.setText("Fetching images")
                    resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
                    i = 0

                    for resource in resources:
                        text_set = str("Downloading image " + str(i))
                        text_set = text_set.encode('utf-8')
                        self.status_bar_text.setText(str(text_set))
                        if resource['initiatorType'] == 'img':
                            filename = str('temp/images/') + str('image') + str(i) + str('.png')
                            res = requests.get(resource['name'], stream=True)
                            if res.status_code == 200:
                                with open(filename, 'wb') as f:
                                    shutil.copyfileobj(res.raw, f)
                                try:
                                    pixmap = QPixmap(filename)
                                    button_image = QIcon(pixmap)
                                    widget_to_update = (("image_") + str(i))
                                    getattr(self, widget_to_update).setStyleSheet(
                                        f"QPushButton {{ background-image: url('{filename}'); }}")
                                    saved_image = Image.open(filename)
                                    width, height = saved_image.size
                                    getattr(self, widget_to_update).setMinimumHeight(int(height))
                                    getattr(self, widget_to_update).setMinimumWidth(int(width))
                                    getattr(self, widget_to_update).setMaximumHeight(int(height))
                                    getattr(self, widget_to_update).setMaximumWidth(int(width))
                                except:
                                    pass

                            i = i + 1

                except Exception as e:
                    print(e)
                    notify_in_thread(title_prompt="Failed", message_prompt='Something went wrong')
                    self.status_bar_text.setText("Something went wrong")

            if self.videos_toggle.isChecked() == True:
                self.status_bar_text.setText("Scraping videos")
                try:
                    self.status_bar_text.setText("Fetching video using YT-dlp")
                    ydl_opts = {'outtmpl': 'temp/videos/video.%(ext)s'}
                    zxt = url.strip()
                    self.status_bar_text.setText("Downloading video")

                    with YoutubeDL(ydl_opts) as ydl:
                        terminal_output = ydl.download([zxt])

                    cap = cv2.VideoCapture('temp/videos/video.mp4')
                    ret, frame = cap.read()
                    height, width, channel = frame.shape
                    bytesPerLine = 3 * width
                    qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    label = QLabel(" ", parent=self)
                    label.setPixmap(QPixmap.fromImage(qImg))
                    self.video_layout_0.addWidget(label)


                except Exception as e:
                    print(e)
                    notify_in_thread(title_prompt="Failed", message_prompt='Something went wrong')

            notify_in_thread(title_prompt="Scraping", message_prompt=('Finished Scraping'))
            self.status_bar_text.setText("Finished scraping")
            self.scrape_layout.removeWidget(self.scrape_button)
            self.scrape_button.deleteLater()
            go_to_next_page()



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
my_pixmap = QPixmap("fluorite.ico")
my_icon = QIcon(my_pixmap)
window.setWindowTitle(" ")
window.setWindowIcon(my_icon)
window.show()
app.exec()
