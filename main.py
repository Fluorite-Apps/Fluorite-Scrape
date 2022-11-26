# Imports
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import validators
import time
from bs4 import BeautifulSoup

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
    scrape_what = input("What do you want to scrape?\n1 = Text\n2 = Images\n3 = Videos (coming soon)\n")
    scrape_what_list = ['1', '2']
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
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("Sleeping")
    time.sleep(5)
    print("Scraping")
    if int(scrape_what) == int(1):
        print(driver.find_element(By.XPATH, "/html/body").text)
    if int(scrape_what) == int(2):
        resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
        for resource in resources:
            if resource['initiatorType'] == 'img':
                print(resource['name'])



cli_main_menu()
