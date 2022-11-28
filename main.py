# Imports
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import youtube_dl
import os.path
import sys
import os
from ui_window import *
from PySide6.QtGui import *
import subprocess
import re
from PySide6 import QtCore, QtWidgets, QtGui

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


# Global Variables
global url

# Create all files and folders if they don't exist
if not os.path.isdir('temp/'):
    os.mkdir('temp/')
if not os.path.isdir('temp/images/'):
    os.mkdir('temp/images/')
if not os.path.isdir('temp/videos/'):
    os.mkdir('temp/videos/')


def notify_function(title_prompt, message_prompt):
    notification.notify(
        title=(title_prompt),
        message=(message_prompt),
        app_icon="fluorite.ico",
        timeout=10,
    )



# Main Menu
def cli_main_menu():
    # Input Url
    url = input("Enter Url: ")
    url = str(url)
    scrape_what = input("What do you want to scrape?\n1 = Text\n2 = Images\n3 = Videos\n")
    scrape_what_list = ['1', '2', '3']
    # Validate scraping option
    try:
        int(scrape_what)
        if not scrape_what in scrape_what_list:
            print('Invalid Option')
            exit()
    except:
        print("Invalid Option")
        exit()
    cli_scrape(url, scrape_what)

# Scrape the Url
def cli_scrape(url, scrape_what):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
    except:
        exit("Invalid Url")
    print("Sleeping")
    time.sleep(5)
    print("Scraping")
    if int(scrape_what) == int(1):
        try:
            print(driver.find_element(By.XPATH, "/html/body").text)
        except:
            pass

    if int(scrape_what) == int(2):
        try:
            resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
            for resource in resources:
                print(resource['name'])
        except:
            pass
    if int(scrape_what) == int(3):
        try:
            ydl_opts = {}
            zxt = url.strip()
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([zxt])
        except:
            print("We cannot scrape videos from this url currently")
    print("Not what you were looking for? This program may not be able to scrape this website (yet)")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None , *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(1150, 800)

        GlobalBlur(self.winId(),Dark=True,QWidget=self)

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

        self.scrape_button = custompushbutton('SCRAPE', parent=self)
        self.scrape_button.setMinimumHeight(70) # was 91
        self.scrape_button.setFixedWidth(182) # was 251
        self.scrape_layout.addWidget(self.scrape_button, Qt.AlignCenter, Qt.AlignCenter)
        self.scrape_button.clicked.connect(lambda: scrape_gui())


        def scrape_gui():
            # Deleting all temp files
            filelist = [f for f in os.listdir('temp/images/') if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join('temp/images/', f))
            with open('temp/text.txt', 'w+') as f:
                f.truncate(0)
                f.seek(0)
            # Scraping
            global url
            url = self.url_input.text()
            notify_function(title_prompt="Scraping", message_prompt=('Started to scrape website'))
            try:
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
            except:
                notify_function(title_prompt="Failed", message_prompt=('Invalid Url or invalid Chrome driver'))
            time.sleep(5)

            if self.text_toggle.isChecked() == True:
                try:
                    with open('temp/text.txt', 'w+') as web_text:
                        web_text.truncate(0)
                        web_text.seek(0)
                        web_text.write(driver.find_element(By.XPATH, "/html/body").text)
                except:
                    notify_function(title_prompt="Failed", message_prompt=('Something went wrong'))

            if self.images_toggle.isChecked() == True:
                    try:
                        resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
                        i = 0
                        for resource in resources:
                            if resource['initiatorType'] == 'img':
                                filename = str('temp/images/') + str('image') + str(i) + str('.png')
                                res = requests.get(resource['name'], stream=True)
                                if res.status_code == 200:
                                    with open(filename, 'wb') as f:
                                        shutil.copyfileobj(res.raw, f)
                                i = i + 1
                    except:
                        notify_function(title_prompt="Failed", message_prompt=('Something went wrong'))

            notify_function(title_prompt="Scraping", message_prompt=('Finished Scraping'))




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('  ')
my_pixmap = QPixmap("fluorite.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()





