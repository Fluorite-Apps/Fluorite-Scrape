# Imports
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import youtube_dl

# Main Menu
def cli_main_menu():
    # Input Url
    url = input("Enter Url: ")
    url = str(url)
    # Validate Url
    # if not validators.url(url) == True:
    #     print("Invalid Url")
    #     exit()
    # Input scraping option
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





cli_main_menu()
