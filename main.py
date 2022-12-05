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

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QWidget, QMessageBox, QComboBox)

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

# Global Variables
global url

# Create all files and folders if they don't exist
if not os.path.isdir('temp/'):
    os.mkdir('temp/')
if not os.path.isdir('temp/images/'):
    os.mkdir('temp/images/')
if not os.path.isdir('temp/videos/'):
    os.mkdir('temp/videos/')


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
            # for f in filelist:
            #     os.remove(os.path.join('temp/videos/*', f))
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
            except:
                notify_in_thread(title_prompt="Failed", message_prompt=('Invalid Url or invalid Chrome driver'))
                self.status_bar_text.setText("Invalid Url or invalid Chrome driver")
            time.sleep(5)

            if self.text_toggle.isChecked() == True:
                self.status_bar_text.setText("Scraping text")
                try:
                    with open('temp/text.txt', 'w+', encoding="utf-8") as web_text:
                        web_text.truncate(0)
                        web_text.seek(0)
                        self.status_bar_text.setText("Writing text to file temp/text.txt")
                        web_text.write(str(driver.find_element(By.XPATH, "/html/body").text))
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
                            i = i + 1
                except:
                    traceback.print_exc()
                    notify_in_thread(title_prompt="Failed", message_prompt='Something went wrong')
                    self.status_bar_text.setText("Something went wrong")

            if self.videos_toggle.isChecked() == True:
                self.status_bar_text.setText("Scraping videos")
                try:
                    self.status_bar_text.setText("Fetching video using YT-dlp")
                    ydl_opts = {'outtmpl': 'temp/videos/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s'}
                    zxt = url.strip()
                    self.status_bar_text.setText("Downloading video")
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([zxt])
                except:
                    notify_in_thread(title_prompt="Failed", message_prompt='Something went wrong')

            notify_in_thread(title_prompt="Scraping", message_prompt=('Finished Scraping'))
            self.status_bar_text.setText("Finished scraping")




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('  ')
my_pixmap = QPixmap("fluorite.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()
